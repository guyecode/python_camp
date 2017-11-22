var webpage = require('webpage')
var page = webpage.create()
var url = 'http://item.jd.com/782353.html'

page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
page.open(url, function(status){
    console.log(status);
    if (status === "success") {
        // page.render('782353.png');
        console.log(document.getElementsByClassName('price J-p-782353')[0]);
        var price = document.getElementsByClassName('price J-p-782353')[0].innerText;
        console.log(price);
        phantom.exit()
    }
    // setTimeout(function() {
    //     var result = page.evaluate(function() {
    //         var price = document.getElementsByClassName('price J-p-782353')[0].innerText;
    //         console.log(price);
    //         phantom.exit();
    //     });
    // }, 12000);
});