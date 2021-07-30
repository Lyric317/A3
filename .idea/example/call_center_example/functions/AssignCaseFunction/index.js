exports.handler = async (event) => {
    const response = {
        case: event.case,
        message: `${event.message} assigned...`
    };
    return response;
};