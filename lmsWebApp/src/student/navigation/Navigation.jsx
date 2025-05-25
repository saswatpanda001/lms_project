import React from 'react'
import { useNavigate } from 'react-router-dom'
const Navigation = () => {
    const pathname = window.location.pathname
    console.log(pathname)
    const nav = useNavigate()

    const handleLogout = () => {
        
        localStorage.removeItem('access');
        localStorage.removeItem('email');
        localStorage.removeItem('refresh');
        localStorage.removeItem('status');
        localStorage.removeItem('user_id');
        localStorage.removeItem('username');

        
        nav("/login")


    
    }

    return (
        <nav class="bg-white shadow-sm">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex justify-between h-16">
                        <div class="flex items-center">
                            <div class="flex-shrink-0 flex items-center">
                                <i class="fas fa-graduation-cap text-primary text-2xl mr-2"></i>
                                <span class="text-xl font-bold text-dark">EduConnect</span>
                            </div>
                        </div>
                        <div class="hidden md:ml-6 md:flex md:items-center md:space-x-8">
                            <a href="/student/dashboard" class="text-primary px-3 py-2 font-medium">Dashboard</a>
                            <a href="/student/courses" class="text-primary px-3 py-2 font-medium">Courses</a>
                            <a href="/student/assignment" class="text-primary px-3 py-2 font-medium">Assignments</a>
                            <a href="/student/grades" class="text-primary px-3 py-2 font-medium">Grades</a>
                            <div class="flex items-center ml-4">
                                <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Profile" class="w-8 h-8 rounded-full mr-2"/>
                                <span class="text-primary px-3 py-2 font-mediums">John Doe</span>
                            </div>
                            <a onClick={() => handleLogout()} class="text-primary px-3 py-2 font-medium">Logout</a>
                        </div>
                    </div>
                </div>
            </nav>


    )
}

export default Navigation;
