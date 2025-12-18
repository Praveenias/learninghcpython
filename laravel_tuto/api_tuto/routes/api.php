<?php


use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::apiresource('categories','App\Http\Controllers\Api\CategoryController');
// Route::get('categories','App\Http\Controllers\Api\CategoryController@index');
// Route::get('categories/{category}','App\Http\Controllers\Api\CategoryController@show');
// Route::post('categories','App\Http\Controllers\Api\CategoryController@store');
// Route::put('categories/{category}','App\Http\Controllers\Api\CategoryController@update');
// Route::delete('categories/{category}','App\Http\Controllers\Api\CategoryController@destroy');

Route::get('products','App\Http\Controllers\Api\ProductController@index');