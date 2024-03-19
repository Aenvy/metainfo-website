import { Box } from 'grommet'

const colorSchemaReady = {
  before: "green",
  current: "white",
  after: "gray",
}

const colorSchemaFailed = {
  before: "green",
  current: "red",
  after: "gray",
}

function statusToBackgroundColor(states, status, state, colorSchema) {
  const index = states.indexOf(state)
  const currentIndex = states.indexOf(status)
  if (index < currentIndex) {
    return colorSchema.before
  } else if (index === currentIndex) {
    return colorSchema.current
  } else {
    return colorSchema.after
  }
}

function statusToBorder(states, status, state) {
  const index = states.indexOf(state)
  const currentIndex = states.indexOf(status)
  if (index === currentIndex) {
    return {
      color: "brand",
      size: "medium",
    }
  } else {
    return false
  }
}

function failedStatusToLabel(failedStates, status, state) {
  const readyStates = failedStates.map(state => {
    const splitState = state.split(" ")
    if (splitState.length === 2 && splitState[1] === "Failed") {
      return splitState[0] + " Ready"
    } else {
      return state
    }
  })

  const index = failedStates.indexOf(state)
  const currentIndex = failedStates.indexOf(status)

  if (index === currentIndex) {
    return state
  } else {
    return readyStates[index]
  }
}

function stateToBox(state, index) {
  return <Box
    key={`${index}-${state}`}
    style={{ textAlign: "center" }}
    align="center"
    justify="center"
    width="small"
    height="xxsmall"
    margin="xxsmall"
    pad="xxsmall"
    background={state.background}
    border={state.border}
  >
    {state.label}
  </Box>
}

function linesToStates(lines, status) {
  for (let line of lines) {
    if (line.states.indexOf(status) >= 0) {
      return line.generator(line.states, status)
    }
  }

  return [
    {
      label: status,
      background: "black",
      border: false,
    }
  ]
}

function generateLineStateFailed(states, status) {
  return states.map(state => {
    return {
      label: failedStatusToLabel(states, status, state),
      background: statusToBackgroundColor(states, status, state, colorSchemaFailed),
      border: false,
    }
  })
}

function generateLineStateReady(states, status) {
  return states.map(state => {
    return {
      label: state,
      background: statusToBackgroundColor(states, status, state, colorSchemaReady),
      border: statusToBorder(states, status, state),
    }
  })
}

const MetainfoStatus = ({ status, statusLines }) => {
  return (
    <Box direction="row">{
      linesToStates(statusLines, status).map(stateToBox)
    }</Box>
  )
}

export default MetainfoStatus
export {
  generateLineStateFailed,
  generateLineStateReady,
  MetainfoStatus,
}
