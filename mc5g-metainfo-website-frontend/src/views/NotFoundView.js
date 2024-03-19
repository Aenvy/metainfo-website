import {
  PageContent,
  PageHeader,
  Text,
} from 'grommet'
import {
  useEffect,
} from 'react'

const NotFoundView = ({ setExtraIcons, ...props }) => {
  useEffect(() => {
    setExtraIcons([])
  }, [setExtraIcons])

  return (
    <PageContent {...props}>
      <PageHeader title="Not found" />
      <Text>This URL does not exist.</Text>
    </PageContent>
  )
}

export default NotFoundView
