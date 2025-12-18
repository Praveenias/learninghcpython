<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Http\Requests\StoreCategoryRequest;
use App\Http\Resources\CategoryResource;
use App\Models\Category;
use Symfony\Component\HttpFoundation\Response;

class CategoryController extends Controller
{
    //
    public function index(){
        return CategoryResource::collection(Category::all());

    }

    public function show(Category $category){
         return new CategoryResource($category);

    }

    public function store(StoreCategoryRequest $req){ 
        
        $data = $req->all();
        if($req->hasFile('photo')){
            $file = $req->file('photo');
            $name = 'categories/'.uniqid().'.'.$file->extension();
            $file->storePubliclyAs('public',$name);
            $data['photo']=$name;
        }
        $category = Category::create($data);
        return new CategoryResource($category);

    }

    public function update(Category $category,StoreCategoryRequest $req){
        $category->update($req->all());
        return new CategoryResource($category);
    }

    public function destroy(Category $category){
        $category->delete();
        return response(null,Response::HTTP_NO_CONTENT);
    }
}
