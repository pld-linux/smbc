Summary:	Simple Samba Commander
Summary(pl.UTF-8):	Konsolowa przeglądarka otoczenia sieciowego
Name:		smbc
Version:	1.2.2
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/smbc/%{name}-%{version}.tgz
# Source0-md5:	f5c1a16ea0378d96cb27e8d96229e8ad
Source1:	%{name}.desktop
URL:		http://smbc.airm.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libsmbclient-devel >= 3.0
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	popt-devel
BuildRequires:	sed >= 4.0
Requires:	samba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple Samba Commander is a text mode SMBnet commander. In SMBC, you
can browse the local network or you can use the search function to
find the files. You can also download and upload files or all
directories to your computer or create remote and local directories.
SMBC has a resume function and supports UTF-8 characters.

%description -l pl.UTF-8
Simple Samba Commander jest prostą tekstową przeglądarką sieci opartej
o protokół SMB. Za pomocą SMBC można przeglądać sieć lokalną lub w
poszukiwaniu konkretnego pliku wykorzystać funkcję wyszukiwania.
Dostępna jest również funkcja pobierania oraz wysyłania plików jak i
całych katalogów. SMBC zawiera funkcje automatycznego wznawiania
połączenia, obsługę wielu języków wspiera również standard kodowania
znaków UTF8.

%prep
%setup -q
rm -rf src/CVS
sed -i 's@<curses.h>@<ncurses/curses.h>@' src/*

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ README doc/sample.smbcrc
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_infodir}/*.info*
%{_mandir}/man1/smbc.*
%{_mandir}/man1/smbcrc.*
