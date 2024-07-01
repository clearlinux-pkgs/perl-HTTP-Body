#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-HTTP-Body
Version  : 1.23
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/G/GE/GETTY/HTTP-Body-1.23.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GE/GETTY/HTTP-Body-1.23.tar.gz
Summary  : 'HTTP Body Parser'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-HTTP-Body-license = %{version}-%{release}
Requires: perl-HTTP-Body-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Headers)
BuildRequires : perl(HTTP::Request::Common)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(URI)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution HTTP-Body,
version 1.23:
HTTP Body Parser

%package dev
Summary: dev components for the perl-HTTP-Body package.
Group: Development
Provides: perl-HTTP-Body-devel = %{version}-%{release}
Requires: perl-HTTP-Body = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Body package.


%package license
Summary: license components for the perl-HTTP-Body package.
Group: Default

%description license
license components for the perl-HTTP-Body package.


%package perl
Summary: perl components for the perl-HTTP-Body package.
Group: Default
Requires: perl-HTTP-Body = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Body package.


%prep
%setup -q -n HTTP-Body-1.23
cd %{_builddir}/HTTP-Body-1.23
pushd ..
cp -a HTTP-Body-1.23 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-HTTP-Body
cp %{_builddir}/HTTP-Body-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-HTTP-Body/62be08a7b6bd3192c9c42142bc39e2e42d3aae5a || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

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
/usr/share/package-licenses/perl-HTTP-Body/62be08a7b6bd3192c9c42142bc39e2e42d3aae5a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
