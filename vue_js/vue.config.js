const path = require('path');
const hostname = process.env.HOST_NAME ? process.env.HOST_NAME : 'localhost';

module.exports = {
    devServer: {
        host: hostname,
        port: 8080,
        compress: false,
        hot: true,
        publicPath: `http://${hostname}:8080/`
    },
  chainWebpack: config => {
    config.resolve.alias.set(
      'vue$',
      path.resolve(__dirname, 'node_modules/vue/dist/vue.runtime.esm.js')
    )
  }
};