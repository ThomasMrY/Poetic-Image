var app = getApp();
Page({
  data: {
    images: ["upload.jpg"],
    msg:"",
    upload:false,
    pageBackgroundColor:'#BBBBBB'
  },

  Input: function (e) {
    this.setData({
      msg: e.detail.value
    })
  },
  submit: function () {
    var that = this;
    if(this.data.upload){
    console.log(this.data.msg);
      wx.uploadFile({
        url: 'http://poeticimage.eastus.cloudapp.azure.com:8000/', //仅为示例，非真实的接口地址
        filePath: app.globalData.ImgSrc,
        name: 'file',
        formData: {
          'msg': that.data.msg
        },
        success(res) {
          const data = res.data
          console.log("上传成功！")
        }
      })
    wx.navigateTo({
      url: 'index'
    })
    }
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
          images: [app.globalData.ImgSrc],
pageBackgroundColor:'#4DD52B',
upload:true
        })
      }
    })
  }
})