var timeoutObject;
var timePeriod = 3000;

function autoRedirect() {
	// Initializing the Panel
	oPanel = new YAHOO.widget.Panel("autoRedirectDiv", {visible:false, close:false, fixedcenter:true, width:"400px", height:"180px", draggable:false, constrainttoviewport:true});
	// Rendering the Panel
	oPanel.render();
	
	// CustomEvent which launches an Animation
	alarmEvt = function () {
		// Creating an Animation instance
		progressBar = new YAHOO.util.Anim("warnmessage", {width: {from: 300, to: 0}}, 8);
		progressBar.animate();
//		progressBar.onComplete.subscribe(function () {window.location.href = 'http://localhost/start.html'});
	}
	// CustomEvent fired after the panel is shown 
	oPanel.showEvent.subscribe(alarmEvt);

	//CustomEvent which stops the Animation and reseted it
	alarmEvtStop = function () {
		progressBar.stop(finish, false);
//		progressBar = new YAHOO.util.Anim("warnmessage", {width: {to: 300}}, 0);
//		progressBar.animate();
	}
	
	YAHOO.util.Event.addListener(window, 'mousemove', oPanel.hide, oPanel, true);	
	oPanel.hideEvent.subscribe(alarmEvtStop);
	
	YAHOO.util.Event.addListener(window, "mousemove", resetTimeout);
	timeoutObject = setTimeout("oPanel.cfg.setProperty('visible',true);",timePeriod);
}
/*
function warnung() {
	oPanel.cfg.setProperty("visible",true);
}
*/
function resetTimeout() {
	clearTimeout(timeoutObject);
	timeoutObject = setTimeout("oPanel.cfg.setProperty('visible',true);",timePeriod);
}
