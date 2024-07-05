import { useState, useContext } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { ThemeContext } from './ThemeContext';

import { uiBasePath } from './config';

import AppContainer from './components/AppContainer';

import HomePage from './pages/HomePage';
import ReleasesPage from './pages/ReleasesPage';
import ListArtifactIdsPage from './pages/ListArtifactIdsPage';
import ListArtifactVersionsPage from './pages/ListArtifactVersionsPage';
import MetainfoComponentPage from './pages/MetainfoComponentPage';
import MetainfoProductPage from './pages/MetainfoProductPage';
import MetainfoSolutionPage from './pages/MetainfoSolutionPage';
import MetainfoTestPage from './pages/MetainfoTestPage';
import MetainfoResultPage from './pages/MetainfoResultPage';
import NotFoundPage from './pages/NotFoundPage';
import SearchMetainfoPage from './pages/SearchMetainfoPage';
import ReleaseNotesPage from './pages/ReleaseNotesPage';

export default function Router() {
  const [extraIcons, setExtraIcons] = useState([]);
  const { theme } = useContext(ThemeContext); // Get theme from context

  return (
    <div className={theme}> {/* Apply theme class to the root div */}
      <BrowserRouter basename={uiBasePath}>
        <Routes>
          <Route path='/' element={<AppContainer extraIcons={extraIcons} />}>
            <Route index element={<HomePage setExtraIcons={setExtraIcons} />} />
            <Route path='release-notes'element={<ReleaseNotesPage setExtraIcons={setExtraIcons} />} />
            <Route path='releases/*' element={<ReleasesPage setExtraIcons={setExtraIcons} />} />
            <Route path='components' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='components' />} />
            <Route path='components/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='components' />} />
            <Route path='components/:compArtifactId/:compVersion' element={<MetainfoComponentPage setExtraIcons={setExtraIcons} collection='components' />} />
            <Route path='products' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='products' />} />
            <Route path='products/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='products' />} />
            <Route path='products/:prodArtifactId/:prodVersion/*' element={<MetainfoProductPage setExtraIcons={setExtraIcons} collection='products' />} />
            <Route path='solutions' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='solutions' />} />
            <Route path='solutions/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='solutions' />} />
            <Route path='solutions/:solArtifactId/:solVersion/*' element={<MetainfoSolutionPage setExtraIcons={setExtraIcons} collection='solutions' />} />
            <Route path='tests' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='tests' />} />
            <Route path='tests/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='tests' />} />
            <Route path='tests/:artifactId/:version' element={<MetainfoTestPage setExtraIcons={setExtraIcons} collection='tests' />} />
            <Route path='tests/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='tests' />} />
            <Route path='tests/:artifactId/:version' element={<MetainfoTestPage setExtraIcons={setExtraIcons} collection='tests' />} />
            <Route path='results' element={<ListArtifactIdsPage setExtraIcons={setExtraIcons} collection='results' />} />
            <Route path='results/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='results' />} />
            <Route path='results/:artifactId/:version' element={<MetainfoResultPage setExtraIcons={setExtraIcons} collection='results' />} />
            <Route path='results/:artifactId' element={<ListArtifactVersionsPage setExtraIcons={setExtraIcons} collection='results' />} />
            <Route path='results/:artifactId/:version' element={<MetainfoResultPage setExtraIcons={setExtraIcons} collection='results' />} />
            <Route path='search' element={<SearchMetainfoPage setExtraIcons={setExtraIcons} />} />
            <Route path='*' element={<NotFoundPage setExtraIcons={setExtraIcons} />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  )
}
