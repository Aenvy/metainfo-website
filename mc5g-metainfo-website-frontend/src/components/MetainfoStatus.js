import { Box, Text, Grid } from 'grommet'; 
import { CheckboxSelected, Checkbox } from 'grommet-icons'; 

const colorSchemaReady = {
  before: "rgba(128, 128, 128, 0.7)",
  current: "white",
  after: "rgba(128, 128, 128, 0.7)",
};

const colorSchemaFailed = {
  before: "rgba(128, 128, 128, 0.7)",
  current: "red",
  after: "rgba(128, 128, 128, 0.7)",
};

function statusToBackgroundColor(states, status, state, colorSchema) {
  const index = states.indexOf(state);
  const currentIndex = states.indexOf(status);
  if (index < currentIndex) {
    return colorSchema.before;
  } else if (index === currentIndex) {
    return colorSchema.current;
  } else {
    return colorSchema.after;
  }
}

function statusToBorder(states, status, state) {
  const index = states.indexOf(state);
  const currentIndex = states.indexOf(status);
  if (index === currentIndex) {
    return {
      color: "brand",
      size: "medium",
    };
  } else {
    return false;
  }
}

function failedStatusToLabel(failedStates, status, state) {
  const readyStates = failedStates.map(state => {
    const splitState = state.split(" ");
    if (splitState.length === 2 && splitState[1] === "Failed") {
      return splitState[0] + " Ready";
    } else {
      return state;
    }
  });

  const index = failedStates.indexOf(state);
  const currentIndex = failedStates.indexOf(status);

  if (index === currentIndex) {
    return state;
  } else {
    return readyStates[index];
  }
}

function stateToBox(state, index, status) {
  return (
    <Box
      key={`${index}-${state}`}
      style={{
        textAlign: "center",
        fontWeight: state.current ? "bold" : "normal",
        boxShadow: state.current ? "0 0 10px rgba(0,0,0,0.5)" : "none",
      }}
      align="center"
      justify="center"
      width="small"
      height="xxsmall"
      margin="xxsmall"
      pad="xxsmall"
      background={state.background}
      border={state.border}
    >
      <Grid
        rows={["auto"]} 
        columns={["3/4", "1/4"]}
        gap="small"
      >
        <Box justify="center" align="start">
          <Text style={{ color: 'black' }}>{state.label}</Text>
        </Box>
        <Box justify="center" align="end">
          {state.before && <CheckboxSelected size="medium" color="black" />}
          {state.current && <CheckboxSelected size="medium" color="black" />}
          {state.after && <Checkbox size="medium" color="black" />}
        </Box>
      </Grid>
    </Box>
  );
}

function linesToStates(lines, status) {
  for (let line of lines) {
    if (line.states.indexOf(status) >= 0) {
      return line.generator(line.states, status);
    }
  }

  return [
    {
      label: status,
      background: "black",
      border: false,
    },
  ];
}

function generateLineStateFailed(states, status) {
  return states.map(state => {
    return {
      label: failedStatusToLabel(states, status, state),
      background: statusToBackgroundColor(states, status, state, colorSchemaFailed),
      border: false,
      current: state === status,
      before: states.indexOf(state) < states.indexOf(status),
      after: states.indexOf(state) > states.indexOf(status),
    };
  });
}

function generateLineStateReady(states, status) {
  return states.map(state => {
    return {
      label: state,
      background: statusToBackgroundColor(states, status, state, colorSchemaReady),
      border: statusToBorder(states, status, state),
      current: state === status,
      before: states.indexOf(state) < states.indexOf(status),
      after: states.indexOf(state) > states.indexOf(status),
    };
  });
}

const MetainfoStatus = ({ status, statusLines }) => {
  return (
    <Box direction="row">{
      linesToStates(statusLines, status).map(stateToBox)
    }</Box>
  );
}

export default MetainfoStatus;
export {
  generateLineStateFailed,
  generateLineStateReady,
  MetainfoStatus,
};
