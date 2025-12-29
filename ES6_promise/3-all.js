import uploadPhoto from utils.js;
import createUser from utils.js;

export default function handleProfileSignup(firstName, lastName) {
    return Promise.all([uploadPhoto(), createUser(firstName, lastName)])
        .then((results) => {
        return {
            photo: results[0],
            user: results[1],
        };
        })
        .catch(() => {
        return { photo: null, user: null };
        });
