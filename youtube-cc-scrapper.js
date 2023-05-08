var getSubtitles = require('youtube-captions-scraper').getSubtitles;
var fs = require('fs');

var args = process.argv.slice(2);
var videoId = args[0];
var lang = args[1];


var captions = getSubtitles({
  videoID: videoId, // youtube video id
  lang: lang // default: `en`
}).then(function(captions) {
  // captions is an array of objects
  fs.writeFile('captions.json', JSON.stringify(captions), function(err) {
    if (err) throw err;
    console.log('captions saved!');
  });
});


