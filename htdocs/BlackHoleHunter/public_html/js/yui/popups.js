// YUI for the 'popups'    	
YAHOO.namespace("quotes");
function init() {
	YAHOO.quotes.loecher = new YAHOO.widget.Panel("loecher", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.loecher.render();
	YAHOO.util.Event.addListener("quote1", "click", YAHOO.quotes.loecher.show, YAHOO.quotes.loecher, true);
	YAHOO.util.Event.addListener("quote8", "click", YAHOO.quotes.loecher.show, YAHOO.quotes.loecher, true);
	YAHOO.util.Event.addListener("quote19", "click", YAHOO.quotes.loecher.show, YAHOO.quotes.loecher, true);
	YAHOO.util.Event.addListener("quote22", "click", YAHOO.quotes.loecher.show, YAHOO.quotes.loecher, true);

	YAHOO.quotes.SLEindeutigkeit = new YAHOO.widget.Panel("SLEindeutigkeit", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.SLEindeutigkeit.render();
	YAHOO.util.Event.addListener("quote2", "click", YAHOO.quotes.SLEindeutigkeit.show, YAHOO.quotes.SLEindeutigkeit, true);
	YAHOO.util.Event.addListener("quote3", "click", YAHOO.quotes.SLEindeutigkeit.show, YAHOO.quotes.SLEindeutigkeit, true);

	YAHOO.quotes.supermLoecher = new YAHOO.widget.Panel("supermLoecher", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.supermLoecher.render();
	YAHOO.util.Event.addListener("quote4", "click", YAHOO.quotes.supermLoecher.show, YAHOO.quotes.supermLoecher, true);
	YAHOO.util.Event.addListener("quote21", "click", YAHOO.quotes.supermLoecher.show, YAHOO.quotes.supermLoecher, true);

	YAHOO.quotes.LISA = new YAHOO.widget.Panel("LISA", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.LISA.render();
	YAHOO.util.Event.addListener("quote5", "click", YAHOO.quotes.LISA.show, YAHOO.quotes.LISA, true);
	YAHOO.util.Event.addListener("quote27", "click", YAHOO.quotes.LISA.show, YAHOO.quotes.LISA, true);
	
	YAHOO.quotes.wellenjagd = new YAHOO.widget.Panel("wellenjagd", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.wellenjagd.render();
	YAHOO.util.Event.addListener("quote7", "click", YAHOO.quotes.wellenjagd.show, YAHOO.quotes.wellenjagd, true);

	YAHOO.quotes.DoppelterUrknall = new YAHOO.widget.Panel("DoppelterUrknall", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.DoppelterUrknall.render();
	YAHOO.util.Event.addListener("quote9", "click", YAHOO.quotes.DoppelterUrknall.show, YAHOO.quotes.DoppelterUrknall, true);

	YAHOO.quotes.wellenQuellen = new YAHOO.widget.Panel("wellenQuellen", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.wellenQuellen.render();
	YAHOO.util.Event.addListener("quote10", "click", YAHOO.quotes.wellenQuellen.show, YAHOO.quotes.wellenQuellen, true);
	YAHOO.util.Event.addListener("quote16", "click", YAHOO.quotes.wellenQuellen.show, YAHOO.quotes.wellenQuellen, true);
	YAHOO.util.Event.addListener("quote18", "click", YAHOO.quotes.wellenQuellen.show, YAHOO.quotes.wellenQuellen, true);

	YAHOO.quotes.geistermaterie = new YAHOO.widget.Panel("geistermaterie", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.geistermaterie.render();
	YAHOO.util.Event.addListener("quote13", "click", YAHOO.quotes.geistermaterie.show, YAHOO.quotes.geistermaterie, true);
	YAHOO.util.Event.addListener("quote26", "click", YAHOO.quotes.geistermaterie.show, YAHOO.quotes.geistermaterie, true);

	YAHOO.quotes.GW_Wellen = new YAHOO.widget.Panel("GW_Wellen", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.GW_Wellen.render();
	YAHOO.util.Event.addListener("quote15", "click", YAHOO.quotes.GW_Wellen.show, YAHOO.quotes.GW_Wellen, true);
	YAHOO.util.Event.addListener("show2", "click", YAHOO.quotes.GW_Wellen.show, YAHOO.quotes.GW_Wellen, true);

	YAHOO.quotes.MilchstrZentrum = new YAHOO.widget.Panel("MilchstrZentrum", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.MilchstrZentrum.render();
	YAHOO.util.Event.addListener("quote20", "click", YAHOO.quotes.MilchstrZentrum.show, YAHOO.quotes.MilchstrZentrum, true);

	YAHOO.quotes.pulsare = new YAHOO.widget.Panel("pulsare", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.pulsare.render();
	YAHOO.util.Event.addListener("quote24", "click", YAHOO.quotes.pulsare.show, YAHOO.quotes.pulsare, true);

	YAHOO.quotes.eah = new YAHOO.widget.Panel("eah", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.eah.render();
	YAHOO.util.Event.addListener("quote28", "click", YAHOO.quotes.eah.show, YAHOO.quotes.eah, true);
	YAHOO.util.Event.addListener("show4", "click", YAHOO.quotes.eah.show, YAHOO.quotes.eah, true);

	YAHOO.quotes.GW_IntDetektor = new YAHOO.widget.Panel("GW_IntDetektor", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.GW_IntDetektor.render();
	YAHOO.util.Event.addListener("quote30", "click", YAHOO.quotes.GW_IntDetektor.show, YAHOO.quotes.GW_IntDetektor, true);
	YAHOO.util.Event.addListener("quote31", "click", YAHOO.quotes.GW_IntDetektor.show, YAHOO.quotes.GW_IntDetektor, true);
	
	YAHOO.quotes.gravWellen = new YAHOO.widget.Panel("gravWellen", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.gravWellen.render();
	YAHOO.util.Event.addListener("show1", "click", YAHOO.quotes.gravWellen.show, YAHOO.quotes.gravWellen, true);
	
	YAHOO.quotes.ZirpenNeutronensterne = new YAHOO.widget.Panel("ZirpenNeutronensterne", { fixedcenter:true, width:"1000px", height:"700px", visible:false, constraintoviewport:true } );
	YAHOO.quotes.ZirpenNeutronensterne.render();
	YAHOO.util.Event.addListener("show3", "click", YAHOO.quotes.ZirpenNeutronensterne.show, YAHOO.quotes.ZirpenNeutronensterne, true);
}
YAHOO.util.Event.addListener(window, "load", init);

function gravWellenInsert() {
	var req = new XMLHttpRequest();
	req.open("GET","/eo/gravWellen.txt",true);
	req.onreadystatechange = function() {
		if(req.readyState==4) {
			if(req.status==200) {
				var d = document.getElementById("gravWellenBody")
				d.innerHTML = req.responseText;
			}
		}
	}
	req.send(null);
}

function GW_WellenInsert() {
	var req = new XMLHttpRequest();
	req.open("GET","/eo/GW_Wellen.txt",true);
	req.onreadystatechange = function() {
		if(req.readyState==4) {
			if(req.status==200) {
				var d = document.getElementById("GW_WellenBody")
				d.innerHTML = req.responseText;
			}
		}
	}
	req.send(null);
}

function zirpenInsert() {
	var req = new XMLHttpRequest();
	req.open("GET","/eo/zirpen.txt",true);
	req.onreadystatechange = function() {
		if(req.readyState==4) {
			if(req.status==200) {
				var d = document.getElementById("zirpenBody")
				d.innerHTML = req.responseText;
			}
		}
	}
	req.send(null);
}

function eahInsert() {
	var req = new XMLHttpRequest();
	req.open("GET","/eo/eah.txt",true);
	req.onreadystatechange = function() {
		if(req.readyState==4) {
			if(req.status==200) {
				var d = document.getElementById("eahBody")
				d.innerHTML = req.responseText;
			}
		}
	}
	req.send(null);
}
