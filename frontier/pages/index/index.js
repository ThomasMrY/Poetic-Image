var app = getApp();

Page({
  clickMe: function (){
    var that = this
    if(this.data.choose){
    console.log(this.data.choice)
    wx.request({
      url: "https://iotofmine.oicp.io:55028",
      method: "POST",
      data: {
        msg: that.data.choice
      },
      header: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      success: function (res) {
        console.log("上传成功")
        console.log(res.data)
      },
    })
      wx.navigateTo({
        url: 'next'
      })}
  },
  
  data: {
    choice: 0,
    pageBackgroundColor: '#BBBBBB',
    choose:false,
    items: [
      { value: '1', name: '枯藤老树昏鸦，小桥流水人家' },
      { value: '2', name: '窗前明月光，疑是地上霜'  },
      { value: '3', name: '举头望明月，低头思故乡' }
    ]
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
        console.log(app.globalData.ImgSrc)
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