Name:           ros-hydro-sr-mechanism-model
Version:        1.3.5
Release:        0%{?dist}
Summary:        ROS sr_mechanism_model package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/sr_mechanism_model
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-pr2-mechanism-model
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-sr-hardware-interface
Requires:       tinyxml-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-pr2-mechanism-model
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-sr-hardware-interface
BuildRequires:  tinyxml-devel

%description
sr_mechanism_model contains the transmissions used in the robot model. We needed
specific transmission as we're using our own actuator. We also needed to take
care of the joint 0s which combine the distal and middle phalanges.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Mon Sep 22 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.5-0
- Autogenerated by Bloom

* Fri Sep 19 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.4-0
- Autogenerated by Bloom

