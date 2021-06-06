export const getToken = () => {
  const token = localStorage.getItem('jwt');
  return token ? token.access_token : null;
};

export default { getToken };