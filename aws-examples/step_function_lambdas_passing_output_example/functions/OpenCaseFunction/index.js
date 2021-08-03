exports.handler = async (event) => {
    const response = {
        case: event.inputCaseID,
        message: `Case ${event.inputCaseID} opened...`
    };
    return response;
};