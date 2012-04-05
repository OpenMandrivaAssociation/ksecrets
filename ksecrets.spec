Name:		ksecrets
Version:	4.8.2
Release:	%mkrel 1
Summary:	Secrets management infrastructure for KDE4
# libksecretservice LGPLv2+, most of the rest is GPLv2+
License:	GPLv2+ and LGPLv2+
URL:		https://projects.kde.org/projects/kde/kdeutils/ksecrets
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/%{version}/src/%{name}-%{version}.tar.xz
# mark ksecrets.desktop NoDisplay=true since
# 1.  it lacks Categories and appears in Lost+Found
# 2.  afaict it's not useful in the menu
#     (run without arguments does nothing but show --help)
Patch50:	ksecrets-4.8.1-menu_nodisplay.patch
BuildRequires:	kdelibs4-devel >= 5:4.8.0
BuildRequires:	kdebase4-workspace-devel >= 2:4.8.0
BuildRequires:	pkgconfig(qca2)
Requires:	kdebase4-workspace >= 2:4.8.0
Requires:	qca2-openssl

%description
%{summary}

%files
%doc README
%{_kde_bindir}/ksecrets
%{_kde_bindir}/ksecretsserviced
%{_kde_bindir}/ksecretsync
%{_kde_bindir}/kwl2kss
%{_kde_libdir}/kde4/kcm_ksecretsync.so
%{_kde_libdir}/kde4/kio_ksecretsservice.so
%{_kde_datadir}/applications/kde4/ksecrets.desktop
%{_kde_datadir}/config.kcfg/kcm_ksecretsync.kcfg
%{_datadir}/dbus-1/services/org.kde.ksecretsserviced.service
%{_kde_appsdir}/ksecretsync/ksecretsync.rc
%{_kde_services}/kcm_ksecretsync.desktop
%{_kde_services}/ksecretsserviced.desktop
%{_kde_services}/secrets.protocol

#------------------------------------------------

%define ksecretsservice_major 4
%define libksecretsservice %mklibname ksecretsservice %{ksecretsservice_major}

%package -n %{libksecretsservice}
Summary:	Runtime library for KSecrets
Group:		System/Libraries

%description -n %{libksecretsservice}
Runtime library for KSecrets.

%files -n %{libksecretsservice}
%{_kde_libdir}/libksecretsservice.so.%{ksecretsservice_major}*

#------------------------------------------------

%package devel
Summary:	Development files for %{name}
Requires:	%{libksecretsservice} = %{EVRD}
Requires:	kdelibs4-devel

%description devel
%{summary}.

%files devel
%{_kde_libdir}/libksecretsservice.so
%{_kde_includedir}/ksecretsservice/

#------------------------------------------------

%prep
%setup -q
%patch50 -p1 -b .menu_nodisplay

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

