import {
  TreeDataProvider,
  TreeItem,
  TreeItemIndex,
} from 'react-complex-tree';

function metainfoToTreeItem(collection: String, metainfo): TreeItem {
  const index = `${collection}#${metainfo.ident.groupId}#${metainfo.ident.artifactId}#${metainfo.ident.version}`
  var children = []
  var isFolder = false

  if (collection === 'solutions') {
    children = metainfo.products.map(child => `products#${child.groupId}#${child.artifactId}#${child.version}`)
    isFolder = true
  }
  else if (collection === 'products') {
    children = metainfo.components.map(child => `components#${child.groupId}#${child.artifactId}#${child.version}`)
    isFolder = true
  }

  return {
    index: index,
    data: metainfo.name || metainfo.ident.artifactId,
    isFolder: isFolder,
    children: children,
    canMove: false,
    canRename: false,
  }
}

/**
 * This class is a data source provider for a tree of metainfos.
 *
 * Normally, the view requests the model for additionnal data by calling
 * getTreeItem(). However, the page content also queries the backend to
 * display the metainfo and its children, which makes for a lot of redundant
 * requests and poor UX.
 *
 * Instead, the page fills in the model asynchronously. When the view requests
 * the model for a node, the model waits until the data is supplied by the page
 * and then returns the node. This makes so that the page, which is supposed to
 * know everything it is displaying anyway, can make a couple of quick requests
 * for both itself and the sidebar tree.
 */
export class MetainfoTreeDataProvider implements TreeDataProvider {
  private cache: Record<string, TreeItem>;
  private promises: Record<string, Promise<TreeItem>>;
  private resolves: Record<string, Function>;
  private prefix: string;

  constructor(prefix: string = '/') {
    this.cache = {}
    this.promises = {}
    this.resolves = {}
    this.prefix = prefix
  }

  public async getTreeItem(itemId: TreeItemIndex): Promise<TreeItem> {
    if (this.cache[itemId] !== undefined) {
      // Node is already filled in.
      return this.cache[itemId]
    }

    if (this.promises[itemId] !== undefined) {
      // Node has been requested previously, but is not yet filled in.
      return this.promises[itemId]
    }

    // Node is unknown. Return a promise that will be resolved by populateIndex().
    var promiseResolve;
    const promise = new Promise<TreeItem>((resolve => {
      promiseResolve = resolve
    }));

    this.resolves[itemId] = promiseResolve
    this.promises[itemId] = promise

    return promise
  }

  public populateTreeItem(treeItem: TreeItem) {
    const index : TreeItemIndex = treeItem.index;
    this.cache[index] = treeItem

    if (this.resolves[index] !== undefined) {
      // The view requested this node before the data made it to the cache.
      // Resolve the promise for the node.
      this.resolves[index](treeItem)

      delete this.resolves[index]
      delete this.promises[index]
    }
  }

  public populateTreeItems(treeItems: Array<TreeItem>) {
    for (const treeItem of treeItems) {
      this.populateTreeItem(treeItem)
    }
  }

  public populateMetainfo(collection: string, metainfo) {
    const treeItem = metainfoToTreeItem(collection, metainfo)
    this.populateTreeItem(treeItem)
  }

  public populateMetainfos(collection: string, metainfos: Array<any>) {
    for (const metainfo of metainfos) {
      this.populateMetainfo(collection, metainfo)
    }
  }

  public populateRootMetainfo(collection: string, metainfo) {
    const treeItem = metainfoToTreeItem(collection, metainfo)
    this.populateTreeItem(treeItem)
    this.populateTreeItem({
      index: 'root',
      data: null,
      isFolder: true,
      children: [
        treeItem.index
      ],
      canMove: false,
      canRename: false,
    })
  }

  public buildUiPath(treeItem: TreeItem): any {
    var path: Array<string> = []

    do {
      const treeItemIndex = treeItem.index as string
      path = path.concat(treeItemIndex.split('#').reverse())

      for (const key in this.cache) {
        if (this.cache[key].children.includes(treeItemIndex)) {
          treeItem = this.cache[key]
          break
        }
      }
    } while (treeItem.index !== 'root')

    path = path.reverse()

    if (path.length === 2 && path[0] === 'releases') {
      return { pathname: `${this.prefix}/${path[0]}`, hash: `#${path[1].replace(/\./g, '_')}` }
    }
    return `${this.prefix}${path.join('/')}`
  }
}
