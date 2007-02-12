Summary:	X-Resource extension to provide 'top' like statistics
Summary(pl.UTF-8):   Rozszerzenie X-Resource dostarczające statystyki w stylu "top"
Name:		xrestop
Version:	0.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/Software/xrestop/%{name}-%{version}.tar.gz
# Source0-md5:	8bf9927fab3992290702d28c38b8a4ce
URL:		http://www.freedesktop.org/Software/xrestop
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xrestop uses the X-Resource extension to provide 'top' like statistics
of each connected X11 client's server side resource usage. It is
intended as a developer tool to aid more efficient server resource
usage and debug server side leakage.

It should work with any server supporting the X-Resource extension
(fd.o server and XFree86 4.3+, 'xdpyinfo|grep Resource' should tell
you if your server has it).

%description -l pl.UTF-8
Xrestop używa rozszerzenia X-Resource, aby dostarczyć statystyki w
stylu "top" wykorzystania zasobów po stronie serwera przez każdego
podłączonego klienta X11. Jest to narzędzie przeznaczone dla
programistów, mające pomóc w bardziej wydajnym wykorzystaniu zasobów
serwera i szukaniu wycieków zasobów po stronie serwera.

Powinien działać z każdym serwerem obsługującym rozszerzenie
X-Resource (serwer fd.o oraz XFree86 4.3+ - "xdpyinfo|grep Resource"
pokaże, czy serwer je ma).

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
%doc AUTHORS ChangeLog README 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
