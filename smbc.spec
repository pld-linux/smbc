Summary:	Simple Samba Commander
Summary(pl):	Konsolowa przegl±darka otoczenia sieciowego
Name:		smbc
Version:	1.2.1
Release:	1
License:	GPL
Group:		Applications/Networking	
Source0:	http://dl.sourceforge.net/smbc/%{name}-%{version}.tgz
# Source0-md5:	8e49adf4cb0333bc657d7bbc898769e4
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

%description -l pl
Simple Samba Commander jest prost± tekstow± przegl±dark± sieci opartej
o protokó³ SMB. Za pomoc± SMBC mo¿na przegl±daæ sieæ lokaln± lub w
poszukiwaniu konkretnego pliku wykorzystaæ funkcjê wyszukiwania.
Dostêpna jest równie¿ funkcja pobierania oraz wysy³ania plików jak i
ca³ych katalogów. SMBC zawiera funkcje automatycznego wznawiania
po³±czenia, obs³ugê wielu jêzyków wspiera równie¿ standard kodowania
znaków UTF8.

%prep
%setup -q
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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc FAQ README doc/sample.smbcrc
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_infodir}/*.info*
%{_mandir}/man1/smbc.*
%{_mandir}/man1/smbcrc.*
