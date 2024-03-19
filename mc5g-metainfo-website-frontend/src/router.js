import { useState } from 'react'
import {
  BrowserRouter,
  Route,
  Routes,
} from 'react-router-dom'

import { uiBasePath } from './config'

import AppContainer from './components/AppContainer'

import HomePage from './pages/HomePage'
import ReleasesPage from './pages/ReleasesPage'
import ListArtifactIdsPage from './pages/ListArtifactIdsPage'
import ListArtifactVersionsPage from './pages/ListArtifactVersionsPage'
import MetainfoComponentPage from './pages/MetainfoComponentPage'
import MetainfoProductPage from './pages/MetainfoProductPage'
import MetainfoSolutionPage from './pages/MetainfoSolutionPage'
import MetainfoTestPage from './pages/MetainfoTestPage'
import MetainfoResultPage from './pages/MetainfoResultPage'
import NotFoundPage from './pages/NotFoundPage'
import SearchMetainfoPage from './pages/SearchMetainfoPage'

export default function Router() {
  const [extraIcons, setExtraIcons] = useState([])

  return (
    <BrowserRouter basename={uiBasePath}>
      <Routes>
        <Route path='/' element={<AppContainer extraIcons={extraIcons} />}>
          <Route index element={<HomePage setExtraIcons={setExtraIcons} />} />
          <Route path='releases/*' element={<ReleasesPage setExtraIcons={setExtraIcons} />} />
          <Route path='components' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='components' />} />
          <Route path='components/:groupId/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='components' />} />
          <Route path='components/:compGroupId/:compArtifactId/:compVersion' element={<MetainfoComponentPage setExtraIcons={setExtraIcons} collection='components' />} />
          <Route path='products' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='products' />} />
          <Route path='products/:groupId/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='products' />} />
          <Route path='products/:prodGroupId/:prodArtifactId/:prodVersion/*' element={<MetainfoProductPage setExtraIcons={setExtraIcons} collection='products' />} />
          <Route path='solutions' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='solutions' />} />
          <Route path='solutions/:groupId/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='solutions' />} />
          <Route path='solutions/:solGroupId/:solArtifactId/:solVersion/*' element={<MetainfoSolutionPage setExtraIcons={setExtraIcons} collection='solutions' />} />
          <Route path='tests' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='tests' />} />
          <Route path='tests/:groupId/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='tests' />} />
          <Route path='tests/:groupId/:artifactId/:version' element={<MetainfoTestPage setExtraIcons={setExtraIcons} collection='tests' />} />
          <Route path='results' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='results' />} />
          <Route path='results/:groupId/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='results' />} />
          <Route path='results/:groupId/:artifactId/:version' element={<MetainfoResultPage setExtraIcons={setExtraIcons} collection='results' />} />
          <Route path='search' element={<SearchMetainfoPage setExtraIcons={setExtraIcons} />} />
          <Route path='*' element={<NotFoundPage setExtraIcons={setExtraIcons} />} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}
