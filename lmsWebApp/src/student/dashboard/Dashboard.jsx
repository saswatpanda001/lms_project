import React, { useState } from 'react'
import Navigation from '../navigation/Navigation';
import { useRef } from 'react';
const Dashboard = () => {
  const [collapse,setCollapse] = useState(false);
  const sideBarRef = useRef(null);



  const handleToggle = () => {
    setCollapse(!collapse);
    console.log("toggle")
    if(sideBarRef.current){
      sideBarRef.current.classList.toggle("hidden")
    }

  }

  const handleCollapse = () => {
    setCollapse(true)
    console.log("collapse")
    if(sideBarRef.current){
      sideBarRef.current.classList.remove("hidden")
    }



  }
  
  return (

    <div class="bg-gray-50 font-sans">
      
    <div class="flex h-screen overflow-hidden">

    <div id="sidebar" class="sidebar bg-white shadow-md w-64 flex flex-col">

            <div class="flex items-center justify-between p-4 border-b">
                <div class="flex items-center">
                    <i class="fas fa-graduation-cap text-primary text-2xl mr-3"></i>
                    <span class="logo-text text-xl font-bold text-dark">EduConnect</span>
                </div>
                <button id="toggleSidebar" class="text-gray-500 hover:text-primary">
                    <i class="fas fa-bars"></i>
                </button>
            </div>

            <nav class="flex-1 overflow-y-auto p-4">
                <div class="space-y-2">
                    <a href="#" class="flex items-center p-3 rounded-lg bg-primary text-white">
                        <i class="fas fa-tachometer-alt mr-3"></i>
                        <span class="nav-text">Dashboard</span>
                    </a>
                    <a href="#" class="flex items-center p-3 rounded-lg text-gray-700 hover:bg-gray-100">
                        <i class="fas fa-book mr-3"></i>
                        <span class="nav-text">My Courses</span>
                    </a>
                    <a href="#" class="flex items-center p-3 rounded-lg text-gray-700 hover:bg-gray-100">
                        <i class="fas fa-tasks mr-3"></i>
                        <span class="nav-text">Assignments</span>
                    </a>
                    <a href="#" class="flex items-center p-3 rounded-lg text-gray-700 hover:bg-gray-100">
                        <i class="fas fa-chart-line mr-3"></i>
                        <span class="nav-text">Grades</span>
                    </a>
                    <a href="#" class="flex items-center p-3 rounded-lg text-gray-700 hover:bg-gray-100">
                        <i class="fas fa-calendar-alt mr-3"></i>
                        <span class="nav-text">Schedule</span>
                    </a>
                    <a href="#" class="flex items-center p-3 rounded-lg text-gray-700 hover:bg-gray-100">
                        <i class="fas fa-user mr-3"></i>
                        <span class="nav-text">Profile</span>
                    </a>
                </div>
            </nav>

          
            <div class="p-4 border-t">
                <button id="collapseSidebar" class="w-full flex items-center justify-center p-2 rounded-lg text-gray-700 hover:bg-gray-100">
                    <i class="fas fa-chevron-left"></i>
                    <span class="nav-text ml-2">Collapse</span>
                </button>
            </div>
        </div>

        
        
        <div class="flex-1 flex flex-col overflow-hidden">
          <Navigation/>


            <main class="flex-1 overflow-y-auto p-6 bg-gray-50">

                <div class="bg-white rounded-xl shadow-sm p-6 mb-6">
                    <div class="flex flex-col md:flex-row md:items-center md:justify-between">
                        <div>
                            <h2 class="text-2xl font-bold text-dark mb-2">Welcome back, John!</h2>
                            <p class="text-gray-600">You have 3 upcoming deadlines this week</p>
                        </div>
                        <button class="mt-4 md:mt-0 px-4 py-2 bg-primary text-white rounded-lg hover:bg-indigo-700 transition">
                            View Calendar
                        </button>
                    </div>
                </div>

              
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-6">

                    <div class="bg-white rounded-xl shadow-sm p-6">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg font-semibold text-dark">Enrolled Courses</h3>
                            <span class="px-3 py-1 bg-indigo-100 text-primary text-sm rounded-full">5 Courses</span>
                        </div>
                        <div class="space-y-4">
                            <div class="flex items-center p-3 border rounded-lg hover:bg-gray-50">
                                <div class="w-10 h-10 rounded-md bg-purple-100 flex items-center justify-center mr-3">
                                    <i class="fas fa-calculator text-purple-600"></i>
                                </div>
                                <div>
                                    <h4 class="font-medium">Mathematics</h4>
                                    <p class="text-sm text-gray-500">Dr. Smith</p>
                                </div>
                            </div>
                            <div class="flex items-center p-3 border rounded-lg hover:bg-gray-50">
                                <div class="w-10 h-10 rounded-md bg-blue-100 flex items-center justify-center mr-3">
                                    <i class="fas fa-flask text-blue-600"></i>
                                </div>
                                <div>
                                    <h4 class="font-medium">Chemistry</h4>
                                    <p class="text-sm text-gray-500">Prof. Johnson</p>
                                </div>
                            </div>
                            <div class="flex items-center p-3 border rounded-lg hover:bg-gray-50">
                                <div class="w-10 h-10 rounded-md bg-green-100 flex items-center justify-center mr-3">
                                    <i class="fas fa-book text-green-600"></i>
                                </div>
                                <div>
                                    <h4 class="font-medium">Literature</h4>
                                    <p class="text-sm text-gray-500">Dr. Williams</p>
                                </div>
                            </div>
                        </div>
                        <a href="#" class="mt-4 inline-block text-primary text-sm font-medium hover:underline">View all courses</a>
                    </div>

    
                    <div class="bg-white rounded-xl shadow-sm p-6">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg font-semibold text-dark">Upcoming Deadlines</h3>
                            <span class="px-3 py-1 bg-red-100 text-red-600 text-sm rounded-full">3 Due Soon</span>
                        </div>
                        <div class="space-y-4">
                            <div class="p-3 border rounded-lg hover:bg-gray-50">
                                <div class="flex items-start">
                                    <div class="flex-shrink-0 mt-1">
                                        <div class="w-6 h-6 rounded-full bg-red-100 flex items-center justify-center">
                                            <i class="fas fa-exclamation text-red-500 text-xs"></i>
                                        </div>
                                    </div>
                                    <div class="ml-3">
                                        <h4 class="font-medium">Math Assignment #4</h4>
                                        <p class="text-sm text-gray-500">Due tomorrow at 11:59 PM</p>
                                    </div>
                                </div>
                            </div>
                            <div class="p-3 border rounded-lg hover:bg-gray-50">
                                <div class="flex items-start">
                                    <div class="flex-shrink-0 mt-1">
                                        <div class="w-6 h-6 rounded-full bg-yellow-100 flex items-center justify-center">
                                            <i class="fas fa-clock text-yellow-500 text-xs"></i>
                                        </div>
                                    </div>
                                    <div class="ml-3">
                                        <h4 class="font-medium">Chemistry Lab Report</h4>
                                        <p class="text-sm text-gray-500">Due in 3 days</p>
                                    </div>
                                </div>
                            </div>
                            <div class="p-3 border rounded-lg hover:bg-gray-50">
                                <div class="flex items-start">
                                    <div class="flex-shrink-0 mt-1">
                                        <div class="w-6 h-6 rounded-full bg-blue-100 flex items-center justify-center">
                                            <i class="fas fa-book text-blue-500 text-xs"></i>
                                        </div>
                                    </div>
                                    <div class="ml-3">
                                        <h4 class="font-medium">Literature Essay</h4>
                                        <p class="text-sm text-gray-500">Due next week</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <a href="#" class="mt-4 inline-block text-primary text-sm font-medium hover:underline">View all assignments</a>
                    </div>

                  
                    <div class="bg-white rounded-xl shadow-sm p-6">
                        <div class="flex items-center justify-between mb-4">
                            <h3 class="text-lg font-semibold text-dark">Recent Announcements</h3>
                            <span class="px-3 py-1 bg-gray-100 text-gray-600 text-sm rounded-full">2 New</span>
                        </div>
                        <div class="space-y-4">
                            <div class="p-3 border rounded-lg hover:bg-gray-50">
                                <div class="flex items-start">
                                    <div class="flex-shrink-0 mt-1">
                                        <div class="w-6 h-6 rounded-full bg-green-100 flex items-center justify-center">
                                            <i class="fas fa-bullhorn text-green-500 text-xs"></i>
                                        </div>
                                    </div>
                                    <div class="ml-3">
                                        <h4 class="font-medium">Exam Schedule Update</h4>
                                        <p class="text-sm text-gray-500">From Mathematics Dept. - 2 hours ago</p>
                                    </div>
                                </div>
                            </div>
                            <div class="p-3 border rounded-lg hover:bg-gray-50">
                                <div class="flex items-start">
                                    <div class="flex-shrink-0 mt-1">
                                        <div class="w-6 h-6 rounded-full bg-purple-100 flex items-center justify-center">
                                            <i class="fas fa-info-circle text-purple-500 text-xs"></i>
                                        </div>
                                    </div>
                                    <div class="ml-3">
                                        <h4 class="font-medium">Library Closure Notice</h4>
                                        <p class="text-sm text-gray-500">From Administration - 1 day ago</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <a href="#" class="mt-4 inline-block text-primary text-sm font-medium hover:underline">View all announcements</a>
                    </div>
                </div>

             
                <div class="bg-white rounded-xl shadow-sm p-6">
                    <div class="flex items-center justify-between mb-6">
                        <h3 class="text-lg font-semibold text-dark">Weekly Schedule</h3>
                        <div class="flex space-x-2">
                            <button class="px-3 py-1 border rounded-lg text-gray-700 hover:bg-gray-50">Today</button>
                            <button class="px-3 py-1 border rounded-lg text-gray-700 hover:bg-gray-50">Week</button>
                            <button class="px-3 py-1 border rounded-lg text-gray-700 hover:bg-gray-50">Month</button>
                        </div>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="w-full">
                            <thead>
                                <tr class="text-left border-b">
                                    <th class="pb-3 text-gray-500 font-medium">Time</th>
                                    <th class="pb-3 text-gray-500 font-medium">Mon</th>
                                    <th class="pb-3 text-gray-500 font-medium">Tue</th>
                                    <th class="pb-3 text-gray-500 font-medium">Wed</th>
                                    <th class="pb-3 text-gray-500 font-medium">Thu</th>
                                    <th class="pb-3 text-gray-500 font-medium">Fri</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b">
                                    <td class="py-4 text-gray-500">08:00 - 09:30</td>
                                    <td class="py-4">
                                        <div class="bg-indigo-50 border border-indigo-100 rounded-lg p-2">
                                            <p class="text-sm font-medium text-indigo-700">Mathematics</p>
                                            <p class="text-xs text-indigo-500">Room 302</p>
                                        </div>
                                    </td>
                                    <td class="py-4"></td>
                                    <td class="py-4">
                                        <div class="bg-indigo-50 border border-indigo-100 rounded-lg p-2">
                                            <p class="text-sm font-medium text-indigo-700">Mathematics</p>
                                            <p class="text-xs text-indigo-500">Room 302</p>
                                        </div>
                                    </td>
                                    <td class="py-4"></td>
                                    <td class="py-4"></td>
                                </tr>
                                <tr class="border-b">
                                    <td class="py-4 text-gray-500">10:00 - 11:30</td>
                                    <td class="py-4"></td>
                                    <td class="py-4">
                                        <div class="bg-green-50 border border-green-100 rounded-lg p-2">
                                            <p class="text-sm font-medium text-green-700">Literature</p>
                                            <p class="text-xs text-green-500">Room 105</p>
                                        </div>
                                    </td>
                                    <td class="py-4"></td>
                                    <td class="py-4">
                                        <div class="bg-green-50 border border-green-100 rounded-lg p-2">
                                            <p class="text-sm font-medium text-green-700">Literature</p>
                                            <p class="text-xs text-green-500">Room 105</p>
                                        </div>
                                    </td>
                                    <td class="py-4"></td>
                                </tr>
                                <tr>
                                    <td class="py-4 text-gray-500">13:00 - 14:30</td>
                                    <td class="py-4">
                                        <div class="bg-blue-50 border border-blue-100 rounded-lg p-2">
                                            <p class="text-sm font-medium text-blue-700">Chemistry</p>
                                            <p class="text-xs text-blue-500">Lab 3</p>
                                        </div>
                                    </td>
                                    <td class="py-4"></td>
                                    <td class="py-4">
                                        <div class="bg-blue-50 border border-blue-100 rounded-lg p-2">
                                            <p class="text-sm font-medium text-blue-700">Chemistry</p>
                                            <p class="text-xs text-blue-500">Lab 3</p>
                                        </div>
                                    </td>
                                    <td class="py-4"></td>
                                    <td class="py-4"></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </main>
        </div>
    </div>

   
</div>

    
  )
}

export default Dashboard;





