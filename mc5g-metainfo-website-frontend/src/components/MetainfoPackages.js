import {
  Button,
  DataTable,
  Text,
} from 'grommet'
import {
  Clipboard,
  Download
} from 'grommet-icons'

import { datumValue } from '../utils'

function pkgToButton(type, pkg, metainfo) {
  const repository = datumValue(metainfo, pkg.repository.slice(2, -2))

  if (pkg.path !== undefined) {
    const url = `${repository}/${pkg.path}`
    return (
      <Button title='Download package'>
        <a href={url} target='_blank' rel='noreferrer'>
          <Download />
        </a>
      </Button>
    )
  } else if (type === 'docker') {
    const image = `${repository}/${pkg.name}:${pkg.tag || 'latest'}`
    return (
      <Button title='Copy to clipboard' onClick={() => navigator.clipboard.writeText(image)}>
        <Clipboard />
      </Button>
    )
  } else {
    return null
  }
}

function formatPackage(packages, func) {
  if (!packages) {
    return []
  } else {
    return packages.map(func)
  }
}

function formatPackages(packages, metainfo) {
  if (!packages) {
    return []
  }

  const dockerPackages = formatPackage(packages.docker, pkg => {
    return {
      _key: `docker-${pkg.name}-${pkg.tag}`,
      type: 'docker',
      name: pkg.name,
      version: pkg.tag,
      scope: pkg.scope,
      button: pkgToButton('docker', pkg, metainfo),
    }
  })
  const helmPackages = formatPackage(packages.helm, pkg => {
    return {
      _key: `helm-${pkg.name}-${pkg.version}`,
      type: 'helm',
      name: pkg.name,
      version: pkg.version,
      scope: pkg.scope,
      button: pkgToButton('helm', pkg, metainfo),
    }
  })
  const rawPackages = formatPackage(packages.raw, pkg => {
    return {
      _key: `raw-${pkg.type}-${pkg.name}`,
      type: pkg.type,
      name: pkg.name,
      version: 'N/A',
      scope: pkg.scope,
      button: pkgToButton('raw', pkg, metainfo),
    }
  })
  const yumPackages = formatPackage(packages.yum, pkg => {
    return {
      _key: `yum-${pkg.name}-${pkg.version}`,
      type: 'yum',
      name: pkg.name,
      version: pkg.version,
      scope: pkg.scope,
      button: pkgToButton('yum', pkg, metainfo),
    }
  })
  return [].concat(dockerPackages, helmPackages, rawPackages, yumPackages)
}

const columns = [
  {
    header: 'Type',
    property: 'type',
  },
  {
    header: 'Name',
    property: 'name',
  },
  {
    header: 'Version',
    property: 'version',
  },
  {
    header: 'Scope',
    property: 'scope',
  },
  {
    header: 'Link',
    property: 'button',
    align: 'center',
  },
]

const MetainfoPackages = ({ packages, metainfo }) => {
  const formattedPackages = formatPackages(packages, metainfo)
  if (!Array.isArray(formattedPackages) || formattedPackages.length === 0) {
    return <Text>None.</Text>
  }

  return (
    <DataTable
      columns={columns}
      data={formattedPackages}
      primaryKey='_key'
    />
  )
}

export default MetainfoPackages
