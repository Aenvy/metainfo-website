import {
  Box,
} from 'grommet'
import {
  Cubes,
  Cube,
  Document,
  Catalog,
} from 'grommet-icons'
import { Link } from 'react-router-dom'
import { UncontrolledTreeEnvironment, Tree } from 'react-complex-tree';

function collectionToIcon(collection) {
  switch (collection) {
    case 'releases': return <Catalog />
    case 'solutions': return <Cubes />
    case 'products': return <Cube />
    default: return <Document />
  }
}

const SidebarMetainfoTree = ({ collection, metainfo, dataProvider }) => {
  return (
    <UncontrolledTreeEnvironment
      dataProvider={dataProvider}
      getItemTitle={item => item.data}
      viewState={{
        'metainfo-tree': {
          //selectedItems: [`${collection}#${metainfo.ident.groupId}#${metainfo.ident.artifactId}#${metainfo.ident.version}`],
          expandedItems: [`${collection}#${metainfo.ident.artifactId}#${metainfo.ident.version}`]
        }
      }}
      canDragAndDrop={false}
      canDropOnFolder={false}
      canReorderItems={false}
      renderItemTitle={({ title, item, context, info }
      ) => {
        return (
          <Box direction='row' align='center'>
            {collectionToIcon(item.index.split('#')[0])}
            <Box direction='column' margin='small'>
              <Link to={dataProvider.buildUiPath(item)} style={{textDecoration: 'none'}}>
                <Box style={{ fontWeight: context.isSelected ? 'bolder' : 'normal' }}>{title}</Box>
                <Box style={{ color: 'grey' }}>{item.index.split('#')[2]}</Box>
              </Link>
            </Box>
          </Box>
        )
      }}
    >
      <Tree treeId="metainfo-tree" rootItem="root" treeLabel="Metainfo hierarchical tree" />
    </UncontrolledTreeEnvironment >
  );
}

const SidebarReleaseTree = ({ dataProvider }) => {
  return (
    <UncontrolledTreeEnvironment
      dataProvider={dataProvider}
      getItemTitle={item => item.data}
      viewState={{
        'metainfo-tree': {          
          //selectedItems: [`${collection}#${metainfo.ident.groupId}#${metainfo.ident.artifactId}#${metainfo.ident.version}`],
        }
      }}
      canDragAndDrop={false}
      canDropOnFolder={false}
      canReorderItems={false}
      renderItemTitle={({ title, item, context, info }
      ) => {
        return (
          <Box direction='row' align='center'>
            {collectionToIcon(item.index.split('#')[0])}
            <Box direction='column' margin='small'>
              <Link to={dataProvider.buildUiPath(item)} style={{textDecoration: 'none'}}>
                <Box style={{ fontWeight: context.isSelected ? 'bolder' : 'normal' }}>{title}</Box>
                <Box style={{ color: 'grey' }}>{item.index.split('#')[2]}</Box>
              </Link>
            </Box>
          </Box>
        )
      }}
    >
      <Tree treeId="metainfo-tree" rootItem="root" treeLabel="Metainfo hierarchical tree" />
    </UncontrolledTreeEnvironment >
  );
} 

export { SidebarMetainfoTree, SidebarReleaseTree }