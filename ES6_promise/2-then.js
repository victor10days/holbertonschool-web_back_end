export default function hangleResponseFromAPI(promise) {
    return promise
        .then((response) => {
            return { status: response.status };
        })
        .catch(() => {
            return { status: 500 };
        })
        .finally(() => {
            console.log('Got a response from the API');
        });
}

