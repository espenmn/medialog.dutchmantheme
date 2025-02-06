def image_size(self):
    return self.data["image_size"]


def t_out(self):
    speed = self.data['speed']
    if "t_out" in self.data.keys():
        if self.data["t_out"] > 0:
            return self.data["t_out"] + speed
    return speed + 2000

def get_id(self):
    return "." + self.id

def show_text(self):
    if self.data['showtext'] or self.data['showbody']:
        return True
    return False


def script(self):
    data = self.data
    s_id = self.get_id
    return """require([
      "jquery",
        "++theme++dutchmantheme/javascript/responsiveslides.min",
         ], function () {
         $("%(s_id)s").responsiveSlides({
                maxwidth: %(maxwidth)i,
                nav: "%(nav)s",
                speed: %(speed)i,
                pager: %(pager)s,
                prevText: "<",
                nextText: ">",
            });
        });
        $(window).resize(function(){
      // Setting the heigth of the slides
      var new_height = $("#slider").width()*%(height)i/100;
         var min_height = %(min_height)i;
         var max_height = %(max_height)i;
         if (new_height > max_height) {
          $("#slider").height(max_height);
         } else if (new_height < min_height) {
            $("#slider").height(min_height);
         } else {
            $("#slider").height(new_height);
            }
    }).resize();
    """ % {  "s_id": str(self.id), "nav": data["nav"],
                     "height": data["height"],
                     "max_height": data["max-height"],
                     "min_height": data["min-height"],
                     "maxwidth": data["maxwidth"],
                     "speed": data["speed"],
                     "t_out": data["t_out"],
                     "pager": data["pager"], }



def xscript(self):
    data = self.data
    return """require(["jquery", "++theme++dutchmantheme/javascript/responsiveslides.min.js",], function () {
$("#slider.slider-033090786cd84a61bb88d4ca79cb3a68").responsiveSlides();
});""" % { "s_id": id }


def editmode(self):
    form = self.request.form
    if  '_layouteditor' in form:
        return True
    if  'disabled' in self.data:
        return self.data['disabled']  == False
    return False
