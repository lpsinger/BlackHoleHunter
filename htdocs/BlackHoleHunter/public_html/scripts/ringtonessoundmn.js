soundManager.url = '/soundmanager/soundmanager2.swf'; // override default SWF url
soundManager.debugMode = true;
soundManager.consoleOnly = false;

soundManager.onload = function() {
  // soundManager is initialised, ready to use. Create a sound for this demo page.
 soundManager.createSound({
  id:'ringtone1',
  url:'/ringtones/bach.mp3'
 });
 soundManager.createSound({
  id:'ringtone2',
  url:'/ringtones/number21.mp3'
 });
 soundManager.createSound({
  id:'ringtone3',
  url:'/ringtones/robo.mp3'
 });
 soundManager.createSound({
  id:'ringtone4',
  url:'/ringtones/stone.mp3'
 });
}


