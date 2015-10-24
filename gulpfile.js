// Gulp
var gulp = require('gulp');

// Sass/CSS stuff
var sass = require('gulp-sass');

gulp.task('sass', function () {
    gulp.src('./base/static/styles/scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./base/static/styles/css/'));
});

gulp.task('sass:watch', function(){
    gulp.watch('./base/static/styles/scss/*.scss', ['sass']);
});
