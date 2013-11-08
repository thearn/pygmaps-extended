import math
import pylab
import numpy as np


compiled = """
(function(){var j=window,k=document,l=Math;function n(a,b){return a.width=b}function o(a,b){return a.position=b}function p(a,b){return a.height=b}function q(a,b){return a.zIndex=b}var r="appendChild",s="createElement",t="getCoordinates",u="getView",w="pushLatLngAlt",x="setTimeout",y="style",z="addListener",A="getFeatures",B="InfoWindow",C="maps",D="getPosition",E="setStyleSelector",F="earth",H="prototype",I="setGeometry",J="substring",K="parentNode",L="event";
function M(a){if(!google||!google[F])throw"google.earth not loaded";if(!google[F].isSupported())throw"Google Earth API is not supported on this system";if(!google[F].isInstalled())throw"Google Earth API is not installed on this system";this.l="http://maps.google.com/mapfiles/kml/paddle/red-circle.png";this.b=a;this.k=a.getDiv();this.d=!1;this.f="Earth";this.i=[];this.e={};this.j=null;this.g=0;aa(this);ba(this)}j.GoogleEarth=M;M.MAP_TYPE_ID="GoogleEarthAPI";M[H].o=function(){return this.a};
M[H].getInstance=M[H].o;
function aa(a){var b=a.b,c={tileSize:new google[C].Size(256,256),maxZoom:19,name:a.f,alt:a.f,getTile:function(a,b,c){return c[s]("DIV")}};b.mapTypes.set("GoogleEarthAPI",c);b.setOptions({mapTypeControlOptions:{mapTypeIds:[google[C].MapTypeId.ROADMAP,google[C].MapTypeId.SATELLITE,google[C].MapTypeId.HYBRID,"GoogleEarthAPI"]}});google[C][L][z](b,"maptypeid_changed",function(){if(a.b.getMapTypeId()=="GoogleEarthAPI"){var b;a:{b=RegExp("title=['\\"]?"+a.f+"[\\"']?");for(var c=a.c[K].childNodes,e=0,g;g=c[e];e++)if(b.test(g.innerHTML)){b=g;
break a}b=void 0}c=b;e=c[y].zIndex;g=a.c[K].childNodes;for(var h=0,i;i=g[h];h++)i.__gme_ozi=i[y].zIndex,q(i[y],-1);c.__gme_ozi=e;q(a.c[y],q(c[y],0));c=a.h=k[s]("IFRAME");c.src="javascript:false;";c.scrolling="no";c.frameBorder="0";e=c[y];q(e,-1E5);n(e,p(e,"100%"));o(e,"absolute");e.left=e.top=0;b[r](c);a.c[y].display="";a.d=!0;a.a?N(a):ca(a)}else da(a)})}
function N(a){a.e={};O(a,!0);for(var b=a.a[A]();b.getFirstChild();)b.removeChild(b.getFirstChild());a.g++;for(var b=0,c;c=a.i[b];b++)google[C][L].removeListener(c);b={};c=P;for(var d=0,f;f=c[d];d++)b[f]=Q(a,f);for(c=0;d=b.Marker[c];c++)ea(a,d);for(c=0;d=b.Polygon[c];c++){var e=a,g=d,d=e.a;f=S(e,g);var h=d.createPolygon("");f[I](h);e=T(e,g);f[E](e);e=d.createLinearRing("");h.setOuterBoundary(e);for(var h=e[t](),g=g.getPath().getArray(),e=0,i=void 0;i=g[e];e++)h[w](i.lat(),i.lng(),0);d[A]()[r](f)}for(c=
0;d=b.Polyline[c];c++){h=a;g=d;d=h.a;f=S(h,g);e=d.createLineString("");e.setTessellate(!0);f[I](e);h=T(h,g);f[E](h);h=e[t]();g=g.getPath().getArray();e=0;for(i=void 0;i=g[e];e++)h[w](i.lat(),i.lng(),0);d[A]()[r](f)}for(c=0;d=b.Rectangle[c];c++){var g=a,m=d,d=g.a,h=m.getBounds();f=h.getNorthEast();h=h.getSouthWest();e=S(g,m);e[I](d.createPolygon(""));i=d.createLinearRing("");g=T(g,m);e[E](g);g=i[t]();g[w](f.lat(),f.lng(),0);g[w](f.lat(),h.lng(),0);g[w](h.lat(),h.lng(),0);g[w](h.lat(),f.lng(),0);g[w](f.lat(),
f.lng(),0);e.getGeometry().setOuterBoundary(i);e.setName("placemark");d[A]()[r](e)}for(c=0;d=b.Circle[c];c++){i=a;m=d;d=i.a;f=m.getCenter();g=m.getRadius();h=S(i,m);h[I](d.createPolygon(""));e=d.createLinearRing("");i=T(i,m);h[E](i);for(i=0;i<25;i++){var R=f,v=g,m=14.4*i;v/=6378137;m*=l.PI/180;var G=R.lat()*(l.PI/180),R=R.lng()*(l.PI/180),X=l.cos(v),v=l.sin(v),Y=l.sin(G),G=l.cos(G),Z=X*Y+v*G*l.cos(m),m=new google[C].LatLng(l.asin(Z)/(l.PI/180),(R+l.atan2(v*G*l.sin(m),X-Y*Z))/(l.PI/180));e[t]()[w](m.lat(),
m.lng(),0)}h.getGeometry().setOuterBoundary(e);h.setName("placemark");d[A]()[r](h)}for(c=0;d=b.KmlLayer[c];c++)fa(a,d.getUrl());for(c=0;d=b.GroundOverlay[c];c++)g=d.getBounds(),f=g.getNorthEast(),g=g.getSouthWest(),h=a.a,e=h.createGroundOverlay(""),e.setLatLonBox(h.createLatLonBox("")),e.getLatLonBox().setBox(f.lat(),g.lat(),f.lng(),g.lng(),0),e.setIcon(h.createIcon("")),e.getIcon().setHref(d.getUrl()),h[A]()[r](e)}
function O(a,b){var c=a.b.getCenter(),d=a.a.createLookAt("");d.setRange(l.pow(2,27-a.b.getZoom()));d.setLatitude(c.lat());d.setLongitude(c.lng());d.setHeading(0);d.setAltitude(0);var f=a.a;b?(f.getOptions().setFlyToSpeed(5),f[u]().setAbstractView(d),d.setTilt(15),f.getOptions().setFlyToSpeed(0.75),j[x](function(){f[u]().setAbstractView(d)},200),j[x](function(){f.getOptions().setFlyToSpeed(1)},250)):f[u]().setAbstractView(d)}
function U(a,b){a[0]=="#"&&(a=a[J](1,9));typeof b=="undefined"?b="FF":(b=parseInt(parseFloat(b)*255,10).toString(16),b.length==1&&(b="0"+b));return[b,a[J](4,6),a[J](2,4),a[J](0,2)].join("")}function S(a,b){var c=a.g+"GEV3_"+b.__gme_id;a.e[c]=b;return a.a.createPlacemark(c)}function fa(a,b){var c=a.a;google[F].fetchKml(c,b,function(a){a?c[A]()[r](a):j[x](function(){alert("Bad or null KML.")},0)})}
function ea(a,b){if(b[D]()){var c=a.a,d=S(a,b);b.getTitle()&&d.setName(b.getTitle());var f=c.createIcon("");b.getIcon()?f.setHref(b.getIcon()):f.setHref(a.l);var e=c.createStyle("");e.getIconStyle().setIcon(f);d[E](e);f=c.createPoint("");f.setLatitude(b[D]().lat());f.setLongitude(b[D]().lng());d[I](f);c[A]()[r](d);a.i.push(google[C][L][z](b,"position_changed",function(){var c=a.g+"GEV3_"+b.__gme_id,d=a.e[c],c=a.a.getElementById(c).getGeometry(),d=d[D]();c.setLatitude(d.lat());c.setLongitude(d.lng())}))}}
function T(a,b){var c=a.a.createStyle(""),d=c.getPolyStyle(),f=c.getLineStyle();f.setWidth(V(b,"strokeWeight",3));var e=V(b,"strokeOpacity",1),g=V(b,"fillOpacity",0.3),h=V(b,"strokeColor","#000000"),i=V(b,"fillColor","#000000");f.getColor().set(U(h,e));d.getColor().set(U(i,g));return c}function V(a,b,c){a=a.get(b);return typeof a=="undefined"?c:a}
function ca(a){google[F].createInstance(a.m,function(b){a.a=b;ga(a);N(a)},function(b){ha(a);a.b.setMapTypeId(google[C].MapTypeId.ROADMAP);throw"Google Earth API failed to initialize: "+b;})}
function ga(a){var b=a.a;b.getWindow().setVisibility(!0);var c=b.getNavigationControl();c.setVisibility(b.VISIBILITY_AUTO);c=c.getScreenXY();c.setYUnits(b.UNITS_INSET_PIXELS);c.setXUnits(b.UNITS_PIXELS);c=b.getLayerRoot();c.enableLayerById(b.LAYER_BORDERS,!0);c.enableLayerById(b.LAYER_ROADS,!0);google[C][L][z](a.b,"GEInfoWindowOpened",function(b){if(a.d){var c=a.a.createHtmlStringBalloon("");c.setFeature(a.j);c.setContentString(b.getContent());a.a.setBalloon(c)}});google[F].addEventListener(b.getGlobe(),
"click",function(b){var c=b.getTarget(),e=a.e[c.getId()];if(e){b.preventDefault();for(var b=Q(a,"InfoWindow"),g=0,h;h=b[g];g++)h.close();a.j=c;google[C][L].trigger(e,"click")}})}function ia(a){var b=a.a[u]().copyAsLookAt(a.a.ALTITUDE_RELATIVE_TO_GROUND),c=b.getRange(),c=l.round(27-l.log(c)/l.log(2));!a.b.getZoom()==c?a.b.setZoom(c-1):a.b.setZoom(c);a.b.panTo(new google[C].LatLng(b.getLatitude(),b.getLongitude()))}function da(a){a.d&&(ia(a),j[x](function(){O(a)},50),j[x](function(){ha(a)},2200))}
function ha(a){for(var b=a.c[K].childNodes,c=0,d;d=b[c];c++)q(d[y],d.__gme_ozi);a.h[K].removeChild(a.h);a.h=null;a.c[y].display="none";a.d=!1}
function ba(a){var b=a.k,c=a.c=k[s]("DIV");o(c[y],"absolute");n(c[y],0);p(c[y],0);c.index=0;c[y].display="none";var d=a.n=k[s]("DIV");n(d[y],b.clientWidth+"px");p(d[y],b.clientHeight+"px");o(d[y],"absolute");c[r](d);b=a.m=k[s]("DIV");o(b[y],"absolute");n(b[y],"100%");p(b[y],"100%");d[r](b);a.b.controls[google[C].ControlPosition.TOP_LEFT].push(c);google[C][L][z](a.b,"resize",function(){var b=a.n[y],c=a.k;n(b,c.clientWidth+"px");p(b,c.clientHeight+"px")})}
function Q(a,b){var c=[],d=W[b],f;for(f in d)if(d.hasOwnProperty(f)){var e=d[f];e.get("map")==a.b&&c.push(e)}return c}var W={};function ja(){var a=$,b=google[C][a][H];b.__gme_setMapOriginal=b.setMap;W[a]={};google[C][a][H].setMap=function(b){if(b){if(!this.__gme_id)this.__gme_id=ka++,W[a][this.__gme_id]=this}else delete W[a][this.__gme_id],this.__gme_id=void 0;this.__gme_setMapOriginal(b)}}
for(var P="Marker,Polyline,Polygon,Rectangle,Circle,KmlLayer,GroundOverlay,InfoWindow".split(","),ka=0,la=P,ma=0,$;$=la[ma];ma++)if(ja(),$=="InfoWindow")google[C][B][H].p=google[C][B][H].open,W.InfoWindow={},google[C][B][H].open=function(a,b){if(a){if(!this.__gme_id)this.__gme_id=ka++,W[B][this.__gme_id]=this}else delete W[B][this.__gme_id],this.__gme_id=void 0;google[C][L].trigger(a,"GEInfoWindowOpened",this);this.p(a,b)};})();
"""


def val2hex(v, scale=1.0):
    if not v:
        return "000044"
    j = pylab.get_cmap("jet")
    v = v / scale
    nums = [int(255 * i) for i in j(v)][:3]
    return ''.join(["00" if i == 0 else hex(i)[2:] for i in nums])


class maps(object):

    def __init__(self, centerLat=0, centerLng=0, zoom=7, title="Map",
                 default_view="HYBRID", width=100, height=100):
        self.center = (float(centerLat), float(centerLng))
        self.zoom = int(zoom)
        self.title = title
        self.width = str(int(width))
        self.height = str(int(height))
        self.grids = None
        self.default_view = default_view
        self.paths = []
        self.points = []
        self.radpoints = []
        self.gridsetting = None
        self.coloricon = 'http://chart.apis.google.com/chart?cht=mm&chs=12x16&chco=FFFFFF,XXXXXX,000000&ext=.png'

    def set_grids(self, slat, elat, latin, slng, elng, lngin):
        self.gridsetting = [slat, elat, latin, slng, elng, lngin]

    def add_point(self, lat, lng, color='#FF0000', title=None):
        self.points.append((lat, lng, color[1:], title))

    def add_weighted_path(self, path, weights, scale=1):
        """
        Plots a set of colored path segments based on
        locations and weight values.
        """
        mn, mx = float(min(weights)), max(weights)
        n = len(weights)
        weights_normed = np.array(weights)
        #weights_normed = (weights - mn) / (mx - mn)

        last_w = weights_normed[0]
        lat1 = (path[0][0] + path[1][0]) / 2.
        lon1 = (path[0][1] + path[1][1]) / 2.

        newpath = [path[0], [lat1, lon1]]

        for i in xrange(1, n - 1):
            lat1 = (path[i - 1][0] + path[i][0]) / 2.
            if np.sign(path[i - 1][1]) == np.sign(path[i][1]):
                lon1 = (path[i - 1][1] + path[i][1]) / 2.
            else:
                lat1, lon1 = path[i - 1]

            lat2 = (path[i][0] + path[i + 1][0]) / 2.

            if np.sign(path[i][1]) == np.sign(path[i + 1][1]):
                lon2 = (path[i][1] + path[i + 1][1]) / 2.
            else:
                lat2, lon2 = path[i + 1]

            if weights_normed[i] == last_w:
                newpath.append([lat1, lon1])
                newpath.append(path[i])
                newpath.append([lat2, lon2])
            else:
                col = val2hex(last_w, scale)
                self.add_path(newpath, "#" + col)
                newpath = []
                newpath.append([lat1, lon1])
                newpath.append(path[i])
                newpath.append([lat2, lon2])
            last_w = weights_normed[i]

        if weights_normed[- 1] != last_w:
            col = val2hex(last_w, scale)
            self.add_path(newpath, "#" + col)
            newpath = []

        lat1 = (path[- 2][0] + path[- 1][0]) / 2.
        lon1 = (path[- 2][1] + path[- 1][1]) / 2.
        newpath.append([lat1, lon1])
        newpath.append(path[-1])
        col = val2hex(weights_normed[-1], scale)
        self.add_path(newpath, "#" + col)

    def add_rad_point(self, lat, lng, rad, color='#0000FF'):
        radpoint = {'pt': (lat, lng), 'rad': rad, 'color': color}
        self.radpoints.append(radpoint)

    def add_path(self, path, color='#FF0000', fillcolor='#FF0000', opacity=False):
        path = {'path': path, 'strokeColor': color,
                'fillColor': fillcolor, 'opacity': opacity}
        self.paths.append(path)

    # create the html file which inlcude one google map and all points and
    # paths
    def draw(self, htmlfile=None):
        """
        Creates the header for the HTML file
        """
        if not htmlfile:
            htmlfile = self.title + ".html"
        f = open(htmlfile, 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write(
            '<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />\n')
        f.write(
            '<meta http-equiv="content-type" content="text/html; charset=UTF-8"/>\n')
        f.write('<title>%s </title>\n' % self.title)
        f.write(
            '<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>')
        f.write(
            '<script type="text/javascript" src="https://www.google.com/jsapi"></script>')
        f.write(
            '<script type="text/javascript">%s</script>' % compiled)
        f.write('<script type="text/javascript">\n')
        f.write('google.load("earth", "1");')
        f.write('var map;')
        f.write('var googleEarth;')

        f.write('\tfunction initialize() {\n')
        self.drawmap(f)
        self.drawgrids(f)
        self.drawpoints(f)
        self.drawradpoints(f)
        self.drawpaths(f, self.paths)
        f.write('\t}\n')
        f.write('</script>\n')
        f.write('</head>\n')
        f.write(
            '<body style="margin:0px; padding:0px;" onload="initialize()">\n')
        f.write(
            '\t<div id="map_canvas" style="width: %s%%; height: %s%%;"></div>\n' % (self.width, self.height))
        f.write('</body>\n')
        f.write('</html>\n')
        f.close()

    def drawgrids(self, f):
        if self.gridsetting == None:
            return
        slat = self.gridsetting[0]
        elat = self.gridsetting[1]
        latin = self.gridsetting[2]
        slng = self.gridsetting[3]
        elng = self.gridsetting[4]
        lngin = self.gridsetting[5]
        self.grids = []

        r = [slat + float(x) * latin for x in range(
            0, int((elat - slat) / latin))]
        for lat in r:
            self.grids.append(
                [(lat + latin / 2.0, slng + lngin / 2.0), (lat + latin / 2.0, elng + lngin / 2.0)])

        r = [slng + float(x) * lngin for x in range(
            0, int((elng - slng) / lngin))]
        for lng in r:
            self.grids.append(
                [(slat + latin / 2.0, lng + lngin / 2.0), (elat + latin / 2.0, lng + lngin / 2.0)])

        for line in self.grids:
            self.drawPolyline(f, line, strokeColor="#000000")

    def drawpoints(self, f):
        for point in self.points:
            self.drawpoint(f, point[0], point[1], point[2], point[3])

    def drawradpoints(self, f):
        for rpoint in self.radpoints:
            path = self.getcycle(rpoint['pt'], rpoint['rad'])
            self.drawPolygon(f, path, strokeColor=rpoint['color'])

    def getcycle(self, center, radius):
        cycle = []
        lat, lng = center
        rad = radius  # unit: meter
        d = (rad / 1000.0) / 6378.8
        lat1 = (math.pi / 180.0) * lat
        lng1 = (math.pi / 180.0) * lng

        r = [x * 30 for x in range(12)]
        for a in r:
            tc = (math.pi / 180.0) * a
            y = math.asin(math.sin(lat1) * math.cos(
                d) + math.cos(lat1) * math.sin(d) * math.cos(tc))
            dlng = math.atan2(math.sin(tc) * math.sin(d) * math.cos(
                lat1), math.cos(d) - math.sin(lat1) * math.sin(y))
            x = ((lng1 - dlng + math.pi) % (2.0 * math.pi)) - math.pi
            cycle.append(
                (float(y * (180.0 / math.pi)), float(x * (180.0 / math.pi))))
        return cycle

    def drawpaths(self, f, paths):
        for path in paths:
            if not path['opacity']:
                #fill is false
                self.drawPolyline(
                    f, path['path'], strokeColor=path['strokeColor'])
            else:
                self.drawPolygon(f, path['path'], strokeColor=path[
                                 'strokeColor'], fillColor=path['fillColor'], fillOpacity=path['opacity'])
    #
    # Low level Map Drawing # # # # # #
    #

    def drawmap(self, f):
        f.write('\t\tvar centerlatlng = new google.maps.LatLng(%f, %f);\n' %
                (self.center[0], self.center[1]))
        f.write('\t\tvar myOptions = {\n')
        f.write('\t\t\tzoom: %d,\n' % (self.zoom))
        f.write('\t\t\tcenter: centerlatlng,\n')
        f.write('\t\t\tmapTypeId: google.maps.MapTypeId.%s\n' %
                self.default_view)
        f.write('\t\t};\n')
        f.write(
            '\t\tvar map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);\n')
        f.write('googleEarth = new GoogleEarth(map);')
        f.write('\n')

    def drawpoint(self, f, lat, lon, color, title):
        f.write('\t\tvar latlng = new google.maps.LatLng(%f, %f);\n' %
                (lat, lon))
        f.write('\t\tvar img = new google.maps.MarkerImage(\'%s\');\n' %
                (self.coloricon.replace('XXXXXX', color)))
        f.write('\t\tvar marker = new google.maps.Marker({\n')
        if title != None:
            f.write('\t\ttitle: "' + str(title) + '",\n')
        f.write('\t\ticon: img,\n')
        f.write('\t\tposition: latlng\n')
        f.write('\t\t});\n')
        f.write('\t\tmarker.setMap(map);\n')
        f.write('\n')

    def drawPolyline(self, f, path,
                     clickable=False,
                     geodesic=True,
                     strokeColor="#FF0000",
                     strokeOpacity=1.0,
                     strokeWeight=2
                     ):
        f.write('var PolylineCoordinates = [\n')
        for coordinate in path:
            f.write('new google.maps.LatLng(%f, %f),\n' %
                    (coordinate[0], coordinate[1]))
        f.write('];\n')
        f.write('\n')

        f.write('var Path = new google.maps.Polyline({\n')
        f.write('clickable: %s,\n' % (str(clickable).lower()))
        f.write('geodesic: %s,\n' % (str(geodesic).lower()))
        f.write('path: PolylineCoordinates,\n')
        f.write('strokeColor: "%s",\n' % (strokeColor))
        f.write('strokeOpacity: %f,\n' % (strokeOpacity))
        f.write('strokeWeight: %d\n' % (strokeWeight))
        f.write('});\n')
        f.write('\n')
        f.write('Path.setMap(map);\n')
        f.write('\n\n')

    def drawPolygon(self, f, path,
                    clickable=False,
                    geodesic=True,
                    fillColor="#000000",
                    fillOpacity=0.0,
                    strokeColor="#FF0000",
                    strokeOpacity=1.0,
                    strokeWeight=1
                    ):
        f.write('var coords = [\n')
        for coordinate in path:
            f.write('new google.maps.LatLng(%f, %f),\n' %
                    (coordinate[0], coordinate[1]))
        f.write('];\n')
        f.write('\n')

        f.write('var polygon = new google.maps.Polygon({\n')
        f.write('clickable: %s,\n' % (str(clickable).lower()))
        f.write('geodesic: %s,\n' % (str(geodesic).lower()))
        f.write('fillColor: "%s",\n' % (fillColor))
        f.write('fillOpacity: %f,\n' % (fillOpacity))
        f.write('paths: coords,\n')
        f.write('strokeColor: "%s",\n' % (strokeColor))
        f.write('strokeOpacity: %f,\n' % (strokeOpacity))
        f.write('strokeWeight: %d\n' % (strokeWeight))
        f.write('});\n')
        f.write('\n')
        f.write('polygon.setMap(map);\n')
        f.write('\n\n')
