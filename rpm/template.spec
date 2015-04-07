Name:           ros-indigo-sr-tactile-sensors
Version:        1.4.0
Release:        0%{?dist}
Summary:        ROS sr_tactile_sensors package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/sr_tactile_sensors
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-gazebo-msgs
Requires:       ros-indigo-gazebo-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sr-robot-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-gazebo-msgs
BuildRequires:  ros-indigo-gazebo-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sr-robot-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-visualization-msgs

%description
An interface to the tactile sensors used in the Shadow Dextrous Hand. Also
Contains a virtual set of sensors.

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

