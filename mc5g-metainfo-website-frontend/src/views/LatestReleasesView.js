import React, { useEffect, useState } from 'react';
import { Box, PageContent, Text, CheckBox } from 'grommet';
import { renderState } from '../utils';
import TableArtifacts from '../components/TableArtifacts';

const LatestReleasesView = ({ setExtraIcons, releases, nested = false, showReleaseCandidates, setShowReleaseCandidates,  ...props }) => {
  
  useEffect(() => {
    setExtraIcons([]);
  }, [setExtraIcons]);

  return (
    <PageContent {...props}>
      <h1>Latest releases</h1>
      <CheckBox
        checked={showReleaseCandidates}
        label="Show Release Candidates"
        onChange={() => setShowReleaseCandidates(!showReleaseCandidates)}
      />
      {renderState(releases, releases =>
        releases.map(release => (
          <Box key={release.release}>
            <a href={`#${release.release.replace(/\./g, '_')}`} id={release.release.replace(/\./g, '_')}>
              <Box>
                <Text margin='small' size='large' weight='bolder' color={release.release.includes('RC') ? 'orange' : 'green'}>
                  {release.release}
                </Text>
              </Box>
            </a>
            <TableArtifacts
              collection='products'
              data={release.products}
              sortable={true}
              sort={{ direction: 'asc', property: 'name' }}
              nested={nested}
              nestedPrefix={`${release.release}/`}
            />
          </Box>
        ))
      )}
    </PageContent>
  );
};

export default LatestReleasesView
