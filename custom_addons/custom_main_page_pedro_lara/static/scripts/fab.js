
if(document.getElementById("plb_fab")!=null){
	window.onscroll = function() {scrollFunction()};
}
window.onscroll = function() {scrollFunction()};
function scrollFunction() {
	if(document.getElementById("plb_fab")==null){
		return;
	}
    if (document.body.scrollTop > 180 || document.documentElement.scrollTop > 180) {
        document.getElementById("plb_fab").style.display = "block";
    } else {
        document.getElementById("plb_fab").style.display = "none";
    }
}

function topFunction() {
    document.body.scrollTop = 0; // For Chrome, Safari and Opera 
    document.documentElement.scrollTop = 0; // For IE and Firefox
}