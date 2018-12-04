var app = getApp();
Page({
  data: {
    images: ["upload.jpg"],
    msg:"",
    upload:false,
    pageBackgroundColor:'#BBBBBB',
    bool_display: 'block',
    hiddenflag: true,
  },

  Input: function (e) {
    this.setData({
      msg: e.detail.value
    })
  },
  submit: function () {
    var that = this;
    var back = false;
    this.setData({
      bool_display: 'none',
      hiddenflag: false,
    })
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
          var jdata;
          jdata = JSON.parse(data)
          console.log("上传成功！")
          console.log(jdata)
          console.log(jdata.id)
          app.globalData.id = jdata.id
          app.globalData.Pom1 = jdata.poetry1
          app.globalData.Pom2 = jdata.poetry2
          app.globalData.Pom3 = jdata.poetry3
          back = true
          wx.navigateTo({
            url: 'index'
          })
        }
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