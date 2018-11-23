#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Body
Version  : 1.22
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/G/GE/GETTY/HTTP-Body-1.22.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GE/GETTY/HTTP-Body-1.22.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libh/libhttp-body-perl/libhttp-body-perl_1.22-1.debian.tar.xz
Summary  : 'HTTP Body Parser'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Body-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Headers)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(URI)

%description
This archive contains the distribution HTTP-Body,
version 1.22:
HTTP Body Parser

%package dev
Summary: dev components for the perl-HTTP-Body package.
Group: Development
Provides: perl-HTTP-Body-devel = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Body package.


%package license
Summary: license components for the perl-HTTP-Body package.
Group: Default

%description license
license components for the perl-HTTP-Body package.


%prep
%setup -q -n HTTP-Body-1.22
cd ..
%setup -q -T -D -n HTTP-Body-1.22 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/HTTP-Body-1.22/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Body
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Body/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-HTTP-Body/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Body.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Body/MultiPart.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Body/OctetStream.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Body/UrlEncoded.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Body/XForms.pm
/usr/lib/perl5/vendor_perl/5.28.0/HTTP/Body/XFormsMultipart.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Body.3
/usr/share/man/man3/HTTP::Body::MultiPart.3
/usr/share/man/man3/HTTP::Body::OctetStream.3
/usr/share/man/man3/HTTP::Body::UrlEncoded.3
/usr/share/man/man3/HTTP::Body::XForms.3
/usr/share/man/man3/HTTP::Body::XFormsMultipart.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-HTTP-Body/LICENSE
/usr/share/package-licenses/perl-HTTP-Body/deblicense_copyright
