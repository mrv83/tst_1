
const debug_mode = true;

const Storage = {
    getItem(key) {
        return debug_mode ? JSON.parse(localStorage.getItem(key)) : localStorage.getItem(key)
    },
    setItem(key, value) {
        if (debug_mode) {localStorage.setItem(key, JSON.stringify(value))} else {localStorage.setItem(key, value)}
    },
    removeItem(key) {
        localStorage.removeItem(key)
    },
};

export default Storage;