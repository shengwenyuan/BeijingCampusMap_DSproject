module.exports = {
    devServer: {
        proxy: {
            '/test': {
                target: 'http://127.0.0.1:8000/routeinfo',
                // target: 'https://echarts.apache.org/examples/data/asset/data',
                changeOrigin: true,
                pathRewrite: {
                    '^/test': ''
                }
            }

        }
    },
    css: {
        loaderOptions: {
            postcss: {
                plugins: [
                    require('postcss-pxtorem')({ // 把px单位换算成rem单位
                        rootValue: 75,
                        propList: ['*'],
                        // selectorBlackList: [
                        //     "van-",
                        //     "weui"
                        // ],
                        // 以"van-"和"weui"开头的样式不会自动进行rem转换
                    })
                ]
            }
        }
    },
}