%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240223
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:	Wacom tablet support for Plasma 6
Name:		wacomtablet
Version:	6.4.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/plasma/wacomtablet
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/wacomtablet/-/archive/%{gitbranch}/wacomtablet-%{gitbranchd}.tar.bz2#/wacomtablet-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%{version}/wacomtablet-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	pkgconfig(libwacom)
BuildRequires:	cmake(Plasma5Support)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	pkgconfig(xorg-wacom)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xkbcommon)
# Renamed after 6.0 2025-05-03
%rename plasma6-wacomtablet

BuildSystem:	cmake
BuildOption:	-DBUILD_QCH:BOOL=ON
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Wacom tablet support for Plasma 6

%files -f %{name}.lang
%{_bindir}/kde_wacom_tabletfinder
%{_qtdir}/plugins/kf6/kded/wacomtablet.so
%{_qtdir}/plugins/plasma/kcms/systemsettings_qwidgets/kcm_wacomtablet.so
%{_datadir}/applications/kcm_wacomtablet.desktop
%{_datadir}/applications/kde_wacom_tabletfinder.desktop
%{_datadir}/dbus-1/interfaces/org.kde.Wacom.xml
%{_datadir}/knotifications6/wacomtablet.notifyrc
%{_datadir}/metainfo/org.kde.plasma.wacomtablet.appdata.xml
%{_datadir}/metainfo/org.kde.wacomtablet.metainfo.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.wacomtablet
%{_datadir}/qlogging-categories6/wacomtablet.categories
%{_datadir}/wacomtablet
%{_qtdir}/plugins/plasma5support/dataengine/plasma_engine_wacomtablet.so
%{_datadir}/plasma5support/services/wacomtablet.operations
