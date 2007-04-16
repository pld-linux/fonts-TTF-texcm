Summary:	TeX's Computer Modern Fonts
Summary(pl.UTF-8):	Fonty Computer Modern z TeXa
Name:		fonts-TTF-texcm
Version:	1.0
Release:	1
License:	distributable non-commercially
Group:		Fonts
Source0:	http://www.mozilla.org/projects/mathml/fonts/bakoma/texcm-ttf.zip
# Source0-md5:	7bd39b8860b09c8d5e507dae70484b80
Source1:	http://www.mozilla.org/projects/mathml/fonts/bakoma/license.txt
# Source1-md5:	3ae8d75400a0078db5d7276366c776b0
URL:		http://www.mozilla.org/projects/mathml/fonts/
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         ttffontsdir     %{_fontsdir}/TTF

%description
TeX's Computer Modern Fonts.

%description -l pl.UTF-8
Fonty Computer Modern z TeXa.

%prep
%setup -q -n texcm-ttf
cp -a %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}
cp -a *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc license.txt
%{ttffontsdir}/*.ttf
