var app = getApp();
Page({
  data: {
    images: ["upload.jpg"],
  },
  submit: function () {
    var that = this;
    wx.request({
      url: "https://137.117.33.59:8000",
      method: "POST",
      data: {
        img: that.data.srcs,
        msg:"111"
      },
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      success: function (res) {
        console.log(res.data);
        wx.showToast({
          title: '上传成功！',
          icon: 'success',
          duration: 2000
        })
      },
    })
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
        that.setData({
          images: [app.globalData.ImgSrc]
        })
      }
    })
  }
})