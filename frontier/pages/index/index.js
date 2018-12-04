var app = getApp();

Page({
  clickMe: function (){
    var that = this
    this.setData({
      bool_display: 'none',
      hiddenflag: false,
    })
    if(this.data.choose){
    console.log(this.data.choice)
    wx.request({
      url: "http://poeticimage.eastus.cloudapp.azure.com:8000/",
      method: "POST",
      data: {
        type:"select",
        id:app.globalData.id,
        choice: that.data.choice
      },
      header: {
        "Content-Type": "application/json"
      },
      success: function (res) {
        const data = res.data
        console.log("上传成功！")
        console.log(data)
        console.log(data.id)
        console.log(data.url)
        app.globalData.id = data.id
        wx.downloadFile({
          url: data.url, //仅为示例，并非真实的资源
          success(res) {
            // 下载图片更改链接
            if (res.statusCode === 200) {
              console.log("图片下载成功！！")
              app.globalData.NewImgSrc = res.tempFilePath
              wx.navigateTo({
                url: 'next'
              })
            }
          },
          fail(res){
            console.log(res.statusCode)
            console.log("下载失败！！")
          }
        })
      },
    })
    }
  },
  
  data: {
    choice: 0,
    pageBackgroundColor: '#BBBBBB',
    choose:false,
    items:"",
    bool_display: 'block',
    hiddenflag: true,
  },
  radioChange(e) {
    this.data.choice = e.detail.value
    const items = this.data.items
    
    for (let i = 0, len = items.length; i < len; ++i) {
      items[i].checked = items[i].value === e.detail.value
    }

    this.setData({
      items,
      pageBackgroundColor:'#4DD52B',
      choose:true
    })
  },
    onLoad: function () {
        var _this = this;
      console.log(app.globalData.Pom1)
      console.log(app.globalData.Pom2)
      console.log(app.globalData.Pom3)
        console.log(app.globalData.ImgSrc)
        this.setData({
          items: [
            { value: '1', name: app.globalData.Pom1 },
            { value: '2', name: app.globalData.Pom2 },
            { value: '3', name: app.globalData.Pom3 }
          ]
        })
        if (app.globalData.userInfo) {
            this.setData({
                images: [app.globalData.ImgSrc],
                userInfo: app.globalData.userInfo,
                hasUserInfo: true,
            });
        }
        else if (this.data.canIUse) {
            app.userInfoReadyCallback = function (res) {
                _this.setData({
                    userInfo: res,
                    hasUserInfo: true
                });
            };
        }
        else {
            wx.getUserInfo({
                success: function (res) {
                    app.globalData.userInfo = res.userInfo;
                    _this.setData({
                        userInfo: res.userInfo,
                        hasUserInfo: true
                    });
                }
            });
        }
    },
});