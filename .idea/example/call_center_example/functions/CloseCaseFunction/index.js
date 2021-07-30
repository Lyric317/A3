exports.handler = async (event) => {
    const response = {
        case: event.case,
        status: event.status,
        message: `${event.message} closed...`
    };
    return response;
};