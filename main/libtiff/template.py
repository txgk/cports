pkgname = "libtiff"
pkgver = "4.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-cxx", "--without-x"]
# otherwise it builds nothing
make_dir = "."
hostmakedepends = ["pkgconf"]
makedepends = [
    "jbigkit-devel", "libjpeg-turbo-devel", "liblzma-devel",
    "libzstd-devel", "zlib-devel"
]
pkgdesc = "Library and tools for reading and writing TIFF data files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "libtiff"
url = "http://libtiff.maptools.org"
source = f"http://download.osgeo.org/{pkgname}/tiff-{pkgver}.tar.gz"
sha256 = "0e46e5acb087ce7d1ac53cf4f56a09b221537fc86dfc5daaad1c2e89e1b37ac8"

def post_install(self):
    for f in (self.destdir / "usr/share/man/man3").glob("*.3tiff"):
        self.mv(f, f.with_suffix(".3"))

    self.install_license("COPYRIGHT")

@subpackage("libtiff-static")
def _static(self):
    return self.default_static()

@subpackage("libtiff-devel")
def _devel(self):
    self.depends += makedepends
    return self.default_devel(extra = ["usr/share/doc"])

@subpackage("libtiff-progs")
def _progs(self):
    return self.default_progs()
