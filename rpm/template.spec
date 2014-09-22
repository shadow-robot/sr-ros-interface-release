Name:           ros-hydro-sr-robot-msgs
Version:        1.3.5
Release:        1%{?dist}
Summary:        ROS sr_robot_msgs package

Group:          Development/Libraries
License:        GPL
URL:            http://ros.org/wiki/sr_robot_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-roslib
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-roslib
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs

%description
sr_robot_msgs contains some messages used in the shadow_robot stack.

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
* Mon Sep 22 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.5-1
- Autogenerated by Bloom

* Mon Sep 22 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.5-0
- Autogenerated by Bloom

* Fri Sep 19 2014 Shadow Robot's software team <software@shadowrobot.com> - 1.3.4-0
- Autogenerated by Bloom

