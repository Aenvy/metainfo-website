import {
  Box,
  Button,
  CheckBox,
  Form,
  FormField,
  Layer,
  PageHeader,
} from 'grommet'
import { useState } from 'react'

import { releaseArtifact } from '../api/metainfo'

import { renderState } from '../utils'

const ModalActionRelease = ({ collection, groupId, artifactId, version, onDismiss }) => {
  const [isDraft, setIsDraft] = useState(true)
  const [isDryRun, setIsDryRun] = useState(true)
  const [canSubmit, setCanSubmit] = useState(true)

  const [message, setMessage] = useState(null)

  function onSubmit(value) {
    setMessage(undefined)
    setCanSubmit(false)

    releaseArtifact(collection, groupId, artifactId, version, value).then(response => {
      setMessage('Release process has been started.')
      setCanSubmit(true)
    }).catch(exception => {
      setMessage(exception)
      setCanSubmit(true)
    })
  }

  return (
    <Layer
      onEsc={() => onDismiss()}
      onClickOutside={() => onDismiss()}
    >
      <Box margin='small'>
        <PageHeader title='Start release process...' />
        <Form onSubmit={({value}) => onSubmit(value)} onReset={() => onDismiss()}>
          <FormField name='release' label='Release version' placeholder='x.xxxx.x' required={true} validate={{
            regexp: /[0-9]\.[0-9]{4}\.[0-9]+/,
            message: 'invalid release version',
            status: 'error'
          }} />

          <FormField name='draft' label='Draft release' value={isDraft}>
            <CheckBox name='draft' checked={isDraft} onChange={(event => setIsDraft(event.target.checked))} />
          </FormField>
          <FormField name='dryRun' label='Dry run' value={isDryRun}>
            <CheckBox name='dryRun' checked={isDryRun} onChange={(event => setIsDryRun(event.target.checked))} />
          </FormField>

          <Box direction='row' margin='medium' gap='small' justify='end'>
            <Button type='submit' label='Release' primary={true} disabled={!canSubmit} />
            <Button type='reset' label='Cancel' />
          </Box>
        </Form>
        {
          renderState(message)
        }
      </Box>
    </Layer>
  )
}

export default ModalActionRelease
