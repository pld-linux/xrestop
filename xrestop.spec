Summary:	X-Resource extension to provide 'top' like statistics
Name:		xrestop
Version:	0.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/Software/xrestop/%{name}-%{version}.tar.gz
# Source0-md5:	5ff774ff9cbb5997f0fb68e712dee302
URL:		http://www.freedesktop.org/Software/xrestop
BuildRequires:	ncurses-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Xrestop uses the X-Resource extension to provide 'top' like statistics
of each connected X11 client's server side resource usage. It is
intended as a developer tool to aid more efficient server resource
usage and debug server side leakage.

It should work with any server supporting the X-Resource extension (
fd.o server and XFree86 4.3+, 'xdpyinfo|grep Resource' should tell you
if your server has it ).

%prep
%setup -q

%build
CPPFLAGS="-I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
