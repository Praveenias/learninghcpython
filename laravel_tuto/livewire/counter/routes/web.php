<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

// Route::get('/', function () {
//     return view('welcome');
// });



 
Route::get('/', App\Livewire\Users\ShowUsers::class);
 
Route::get('/users', App\Livewire\Users\CreateUsers::class);
Route::get('user/{user}/edit', \App\Livewire\Users\EditUsers::class)->name('users.edit');

Route::get('datatable',\App\Livewire\Users\Datatable::class)->name('datatable');
