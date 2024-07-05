import {
  Grid,
  Page,
  Box,
  Button,
  Layer,
  Text,
  Spinner
} from 'grommet'
import {
  useEffect,
  useState,
} from 'react'
import {
  Route,
  Routes,
  useParams,
} from 'react-router-dom'
import { Archive } from 'grommet-icons';
import {
  renderState,
} from '../utils'

import MetainfoComponentView from '../views/MetainfoComponentView'
import MetainfoProductView from '../views/MetainfoProductView'
import MetainfoSolutionView from '../views/MetainfoSolutionView'
import NotFoundView from '../views/NotFoundView'
import { SidebarMetainfoTree } from '../components/SidebarMetainfoTree'
import { MetainfoComponentModel } from '../models/MetainfoComponentModel'
import { MetainfoProductModel } from '../models/MetainfoProductModel'
import { MetainfoSolutionModel } from '../models/MetainfoSolutionModel'
import { MetainfoTreeDataProvider } from '../models/MetainfoTreeDataProvider'
import { getInventory } from '../api/metainfo'

const MetainfoSolutionPage = ({ setExtraIcons, collection }) => {
  const { solArtifactId, solVersion } = useParams()

  const [dataProvider] = useState(new MetainfoTreeDataProvider())
  const [dataModel, setDataModel] = useState(undefined)
  const [model] = useState(() => new MetainfoSolutionModel((newDataModel) => {
    setDataModel(newDataModel)
  }, dataProvider))

  const [productIdent, setProductIdent] = useState(undefined)
  const [productDataModel, setProductDataModel] = useState(undefined)
  const [productModel] = useState(() => new MetainfoProductModel((newDataModel) => {
    setProductDataModel(newDataModel)
  }))

  const [componentIdent, setComponentIdent] = useState(undefined)
  const [componentDataModel, setComponentDataModel] = useState(undefined)
  const [componentModel] = useState(() => new MetainfoComponentModel((newDataModel) => {
    setComponentDataModel(newDataModel)
  }))

  const updateProductIdent = (params) => {
    const newProductIdent = {
      collection: 'products',
      artifactId: params.prodArtifactId,
      version: params.prodVersion,
    }

    if (!productIdent ||
      productIdent.collection !== newProductIdent.collection ||
      productIdent.artifactId !== newProductIdent.artifactId ||
      productIdent.version !== newProductIdent.version
    ) {
      setProductIdent(newProductIdent)
    }
  }

  const updateComponentIdent = (params) => {
    const newComponentIdent = {
      collection: 'components',
      artifactId: params.compArtifactId,
      version: params.compVersion,
    }

    if (!componentIdent ||
      componentIdent.collection !== newComponentIdent.collection ||
      componentIdent.artifactId !== newComponentIdent.artifactId ||
      componentIdent.version !== newComponentIdent.version
    ) {
      setComponentIdent(newComponentIdent)
    }
  }
  const [showModal, setShowModal] = useState(false);
  const [inventoryData, setInventoryData] = useState(null);
  useEffect(() => {
    // Call the getInventory function to fetch inventory data
    getInventory(collection, solArtifactId, solVersion)
      .then(inventory => {
        if (inventory !== "{}"){
        // Set inventory data after fetching
          setInventoryData(inventory);
        }
        else{
          setInventoryData("Inventory can not be displayed for this solution, data are missing in metainfos")
        }
      })
      .catch(error => {
        console.error('There was a problem with fetching inventory data:', error);
        setInventoryData("Failed to fetch inventory data");
      });
  }, [collection, solArtifactId, solVersion]);

  useEffect(() => {
    model.load(collection, solArtifactId, solVersion)
  }, [collection, solArtifactId, solVersion, model])

  useEffect(() => {
    productIdent && productModel.load(productIdent.collection, productIdent.artifactId, productIdent.version)
  }, [productIdent, productModel])

  useEffect(() => {
    componentIdent && componentModel.load(componentIdent.collection, componentIdent.artifactId, componentIdent.version)
  }, [componentIdent, componentModel])

  return renderState(model.metainfo, (metainfo) => (
    <Page>
      <Grid columns={['medium', 'flex']}>
        <Box>
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <SidebarMetainfoTree collection={collection} metainfo={metainfo} dataProvider={dataProvider} />
            <Box margin={{ top: 'medium' }}>
              <hr style={{ width: '100%', margin: '0' }} />
              <div style={{ display: 'flex', flexDirection: 'column', paddingLeft: '20px' }}>
                <h3 style={{ marginBottom: '20px', marginLeft: '0' }}>Ansible Inventory</h3>
                <Box direction="row">
                  <Button
                    icon={<Archive />}
                    label="Show Inventory"
                    size="small"
                    margin={{ right: 'xsmall', left: '0', top: '0', bottom: '0' }}
                    primary
                    onClick={() => setShowModal(true)}
                  />
                </Box>
              </div>
            </Box>
          </div>
        </Box>
        {showModal && (
          <Layer
            onEsc={() => setShowModal(false)}
            onClickOutside={() => setShowModal(false)}
          >
            <Box pad="medium">
              <Text weight="bold" margin={{ bottom: 'medium' }}>Ansible Inventory</Text>
              {inventoryData ? (
                <textarea readOnly className="w-100" rows="30" cols="80" value={inventoryData}></textarea>
              ) : (
                <Spinner />
              )}
            </Box>
          </Layer>
        )}
        <Routes>
          <Route index element={
            <MetainfoSolutionView setExtraIcons={setExtraIcons} model={dataModel} alignSelf='top' />
          } />
          <Route path='products/:prodArtifactId/:prodVersion' element={
            <MetainfoProductView setExtraIcons={setExtraIcons} model={productDataModel} alignSelf='top'
              onParams={updateProductIdent}
            />
          } />
          <Route path='products/:prodArtifactId/:prodVersion/components/:compArtifactId/:compVersion' element={
            <MetainfoComponentView setExtraIcons={setExtraIcons} model={componentDataModel} alignSelf='top'
              onParams={updateComponentIdent}
            />
          } />
          <Route path='*' element={<NotFoundView setExtraIcons={setExtraIcons} alignSelf='top' />} />
        </Routes>
      </Grid>
    </Page>
  ))
}

export default MetainfoSolutionPage
