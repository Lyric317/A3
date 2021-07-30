exports.handler = async (event) => {
    // Generate a random number to determine whether the support case has been resolved, then return that value along with the updated message.
    const min = 0;
    const max = 1;
    const myCaseStatus = Math.floor(Math.random() * (max - min + 1)) + min;

    let myMessage = event.message;
    if (myCaseStatus == 1) {
        // Support case has been resolved
        myMessage = `${myMessage} resolved...`;
    } else if (myCaseStatus == 0) {
        // Support case is still open
        myMessage = `${myMessage} unresolved...`;
    }
    const response = {
        case: event.case,
        status: myCaseStatus,
        message: myMessage
    };
    return response;
};