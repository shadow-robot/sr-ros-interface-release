Name:           ros-indigo-shadow-robot
Version:        1.4.0
Release:        0%{?dist}
Summary:        ROS shadow_robot package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/shadow_robot
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-sr-description
Requires:       ros-indigo-sr-example
Requires:       ros-indigo-sr-gazebo-plugins
Requires:       ros-indigo-sr-hand
Requires:       ros-indigo-sr-hardware-interface
Requires:       ros-indigo-sr-mechanism-controllers
Requires:       ros-indigo-sr-mechanism-model
Requires:       ros-indigo-sr-moveit-config
Requires:       ros-indigo-sr-movements
Requires:       ros-indigo-sr-robot-msgs
Requires:       ros-indigo-sr-self-test
Requires:       ros-indigo-sr-tactile-sensors
Requires:       ros-indigo-sr-utilities
BuildRequires:  ros-indigo-catkin

%description
This stack regroups the different ros interfaces developped for Shadow Robot's
Hardware. It provides an interface to both simulated and real hardware.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Apr 07 2015 Shadow Robot's software team <software@shadowrobot.com> - 1.4.0-0
- Autogenerated by Bloom

