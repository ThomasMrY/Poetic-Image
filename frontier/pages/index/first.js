var app = getApp();
Page({

  data: {
    images: [],
    srcs:"upload.jpg"
  },
  submit: function () {
    wx.navigateTo({
      url: 'index'
    })
  },
  onLoad(options) {
  },
  
  submitimg:function() {
    var that = this;
    wx.chooseImage({
      count: 1, // 默认9
      sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
      sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
      success: function (res) {
        // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
        var tempFilePaths = res.tempFilePaths;
        app.globalData.ImgSrc = tempFilePaths[0];
        that.data.srcs = app.globalData.ImgSrc;
        console.log(app.globalData.ImgSrc)
        wx.uploadFile({
          url: 'https://localhost/',      //此处换上你的接口地址
          filePath: tempFilePaths[0],
          name: 'img',
          header: {
            "Content-Type": "multipart/form-data",
            'accept': 'application/json',
            'Authorization': 'Bearer ..'    //若有token，此处换上你的token，没有的话省略
          },
          formData: {
            'user': 'test'  //其他额外的formdata，可不写
          },
          success: function (res) {
            var data = res.data;
            console.log('data');
          },
          fail: function (res) {
            console.log('fail');
          },
        })
      }
    })
  }
})